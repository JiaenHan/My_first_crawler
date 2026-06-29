"""
This module contains the main crawler
"""


import time
import ssl
import certifi
import urllib.request as rq
import urllib.error as er
import url_parser
from craw_state import CrawState


def open_url(url: str) -> str:
    """Extract data from url"""
    response = None
    try:
        req = rq.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        context = ssl.create_default_context(cafile=certifi.where())
        response = rq.urlopen(req, context=context)
        content = response.read()
        content = content.decode(encoding = 'utf-8')
        response.close()
        return content
    except (er.HTTPError, er.URLError) as exc:
        print(f"Cannot open {url}: {exc}")
        if response:
            response.close()
        return ""


def crawler_runner(craw_state: CrawState):
    """The main crawler that craw through urls"""
    while craw_state.still_unseen():
        cur_url = craw_state.get_unseen_url()
        content = open_url(cur_url)
        url_lst = url_parser.parsing_url(content, cur_url)
        # testing
        print("*****")
        print(url_lst)
        # TODO: if not seen, add to unseen urls
        craw_state.change_to_seen(cur_url)
        time.sleep(1)
