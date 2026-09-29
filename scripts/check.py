from html.parser import HTMLParser
from pathlib import Path
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('href','src','poster') and value.startswith('/'):
    path=Path('site')/value.lstrip('/').split('#')[0]
    assert path.exists(),f'Missing asset: {value}'
for path in Path('site').rglob('*.html'):
 text=path.read_text(); Links().feed(text)
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
print('PASS: all HTML local links, metadata, three privacy policies, changelogs and preview videos')
