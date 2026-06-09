"""
This module is responsible for parsing the data
"""


from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def parsing_url(content: str, original_url: str) -> list[str]:
    """Extracting urls from the content"""
    soup = BeautifulSoup(content, 'html.parser')
    url_list = []
    for tag in soup.find_all('a', href = True):
        href = tag['href']
        full_url = urljoin(original_url, href)
        scheme = urlparse(full_url).scheme
        if scheme in ('http', 'https'):
            url_list.append(full_url)

    return url_list
