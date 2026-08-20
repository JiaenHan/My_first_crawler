"""
This module contains the main crawler
"""


import time
import requests
import url_parser
from craw_state import CrawState


def open_url(url: str) -> str:
    """Extract data from url"""
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as exc:
        print(f"Cannot find {url}: {exc}")
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
