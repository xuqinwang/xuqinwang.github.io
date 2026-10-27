"""Check a built site: python3 tests/check_site.py _site (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.headings += 1
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'img':
            assert attrs.get('alt'), 'Image is missing alternative text'


root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
routes = ['index.html', 'publications/index.html', 'experience/index.html',
          'education/index.html', 'skills/index.html', 'cv/index.html', '404.html']
for route in routes:
    path = root / route
    text = path.read_text()
    page = Page()
    page.feed(text)
    assert page.headings == 1, f'{route}: expected one main heading'
    assert 'class="masthead__logo"' in text, f'{route}: missing site logo'
    assert 'rel="icon"' in text, f'{route}: missing favicon'
    assert '{{' not in text and '{%' not in text, f'{route}: unrendered Liquid'
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (root / unquote(url.path).lstrip('/') if url.path.startswith('/')
                  else path.parent / unquote(url.path))
        assert target.is_file() or (target / 'index.html').is_file(), (route, link)

publications = (root / 'publications/index.html').read_text()
assert publications.count('<em>Under review.</em>') == 2
for venue in ['ICLR 2027', 'ICRA 2027', 'Submitted to']:
    assert venue not in publications, f'Submission venue disclosed: {venue}'
for required in ['https://arxiv.org/abs/2609.21804', 'https://videoreloc.github.io/',
                 'https://cinematraj.github.io/']:
    assert required in publications, f'Missing publication status/link: {required}'
home = (root / 'index.html').read_text()
assert 'Xuqin Wang 汪栩沁' in home
assert '/images/profile_ai_sunset.jpg' in home
cv = (root / 'cv/index.html').read_text()
assert 'type="application/pdf"' in cv
assert '/files/CV_XuqinWang_TUM.pdf' in cv
for alias in ['about/index.html', 'about.html', 'resume.html', 'resume/index.html']:
    assert (root / alias).is_file(), f'Missing compatibility redirect: {alias}'
for removed in ['talks', 'teaching', 'portfolio', 'year-archive', 'markdown']:
    assert not (root / removed).exists(), f'Stale template page: {removed}'
print(f'PASS: {len(routes)} pages, local links/assets, submission labels, and redirects')
