from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

from build_guides import run as check_guides
from guide_content import ARTICLES


class Links(HTMLParser):
 def __init__(self,path):
  super().__init__()
  self.path=path

 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key not in ('href','src','poster') or not value: continue
   parsed=urlsplit(value)
   if parsed.scheme or parsed.netloc or not parsed.path: continue
   path=Path('site')/parsed.path.lstrip('/') if parsed.path.startswith('/') else self.path.parent/parsed.path
   assert path.exists(),f'Missing asset in {self.path}: {value}'


check_guides(check=True)
for path in Path('site').rglob('*.html'):
 text=path.read_text(); Links(path).feed(text)
 assert '<title>' in text and 'name="viewport"' in text,path
for lang in ['en','zh-Hans','zh-Hant']:
 text=Path(f'site/{lang}/privacy.html').read_text()
 assert 'RevenueCat' in text and 'Slack' in text
for lang in ['en','zh-Hans','zh-Hant']:
 text=Path(f'site/{lang}/index.html').read_text()
 assert f'/assets/motion/openccman-2-{lang}.mp4' in text and 'autoplay' not in text,lang
 assert Path(f'site/assets/motion/openccman-2-{lang}.mp4').stat().st_size<25*1024*1024,lang
 changelog=Path(f'site/{lang}/changelog.html').read_text()
 assert '2.0' in changelog and '2.1' in changelog and 'https://github.com/gewill/OpenCCman/blob/' in changelog,lang
 assert f'/{lang}/changelog.html' in text,lang
 assert f'/{lang}/guides/' in text,lang
 for slug in ARTICLES:
  guide=Path(f'site/{lang}/guides/{slug}.html').read_text()
  assert guide.count('<h1>')==1 and 'rel="canonical"' in guide,slug
  assert all(f'hreflang="{other}"' in guide for other in ['en','zh-Hans','zh-Hant']),slug
sitemap=ElementTree.parse('site/sitemap.xml').getroot()
urls={entry.text for entry in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
assert len(urls)==27,len(urls)
for lang in ['en','zh-Hans','zh-Hant']:
 assert f'https://openccman.gewill.org/{lang}/guides/' in urls
 for slug in ARTICLES:
  assert f'https://openccman.gewill.org/{lang}/guides/{slug}' in urls
assert all(not url.endswith('.html') for url in urls),urls
print('PASS: local links, metadata, three-language guides, privacy, changelogs and preview videos')
