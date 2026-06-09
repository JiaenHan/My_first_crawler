"""
This module is the entrance of the
crawler
"""


from craw_state import CrawState
import run_crawler


def main() -> None:
    """The starting point of the program"""
    cur_state = CrawState("https://ics.uci.edu")
    run_crawler.crawler_runner(cur_state)


if __name__ == "__main__":
    main()
