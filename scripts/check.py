from html.parser import HTMLParser
from pathlib import Path
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('href','src') and value.startswith('/'):
    path=Path('site')/value.lstrip('/').split('#')[0]
    assert path.exists(),f'Missing asset: {value}'
for path in Path('site').rglob('*.html'):
 text=path.read_text(); Links().feed(text)
 assert '<title>' in text and 'name="viewport"' in text,path
for lang in ['en','zh-Hans','zh-Hant']:
 text=Path(f'site/{lang}/privacy.html').read_text()
 assert 'RevenueCat' in text and 'Slack' in text
print('PASS: all HTML local links, metadata and three privacy policies')
