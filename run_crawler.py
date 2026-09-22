"""
This module contains the main crawler
"""


import time
import requests
import url_parser
from craw_state import CrawState
from db_manager import DBmanager


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


def crawler_runner(craw_state: CrawState, db: DBmanager):
    """The main crawler that craw through urls"""
    try:
        while craw_state.still_has_unseen():
            print(f"Nums left: {len(craw_state._unseen_url)}")
            cur_url = craw_state.get_unseen_url()
            content = open_url(cur_url)
            url_lst = url_parser.parsing_url(content, cur_url)

            for new_url in url_lst:
                if not craw_state.has_seen(new_url):
                    craw_state.add_to_unseen(new_url)
                    db.add_new_url(new_url)
                    db.add_connection(cur_url, new_url)

            craw_state.change_to_seen(cur_url)
            time.sleep(1)
    finally:
        db.close_db()
