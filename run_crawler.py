"""
This module contains the main crawler
"""


import urllib.request
import urllib.error
import url_parser
from craw_state import CrawState


def open_url(url: str) -> str:
    """Extract data from url"""
    response = None
    try:
        response = urllib.request.urlopen(url)
        content = response.read()
        content = content.decode(encoding = 'utf-8')
        response.close()
        return content
    except (urllib.error.HTTPError, urllib.error.URLError):
        if not response:
            response.close()
        return ""


def crawler_runner(craw_state: CrawState):
    """The main crawler that craw through urls"""
    while craw_state.still_unseen():
        cur_url = craw_state.get_unseen_url()
        content = open_url(cur_url)
        url_lst = url_parser.parsing_url(content, cur_url)
        # TODO: if not seen, add to unseen urls
        craw_state.change_to_seen(cur_url)
