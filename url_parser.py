"""
This module is responsible for parsing the data
"""


from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse


def parsing_url(content: str, original_url: str) -> list[str]:
    """Extracting urls from the content"""
    soup = BeautifulSoup(content, 'html.parser')
    url_list = []
    for tag in soup.find_all('a', href = True):
        href = tag['href']
        full_url = urljoin(original_url, href)
        scheme = urlparse(full_url).scheme
        if scheme in ('http', 'https'):
            url_list.append(_normalize_url(full_url))

    return url_list

def _normalize_url(original_url: str) -> str:
    """Returns a normal url without exceptions"""
    parsed = urlparse(original_url)
    path = parsed.path.rstrip("/")
    normalized = parsed._replace(
        scheme=parsed.scheme.lower(),
        netloc=parsed.netloc.lower(),
        path=path,
        fragment=""
    )

    return urlunparse(normalized)

