"""
This module is the entrance of the
crawler
"""


from craw_state import CrawState
from db_manager import DBmanager
import run_crawler


def main() -> None:
    """The starting point of the program"""
    starting_url = "https://ics.uci.edu"
    cur_state = CrawState(starting_url)
    db = DBmanager(starting_url)
    run_crawler.crawler_runner(cur_state, db)


if __name__ == "__main__":
    main()
