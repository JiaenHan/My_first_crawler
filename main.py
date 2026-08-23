"""
This module is the entrance of the
crawler
"""


from craw_state import CrawState
import run_crawler


def main() -> None:
    """The starting point of the program"""
    starting_url = "https://ics.uci.edu"
    cur_state = CrawState(starting_url)
    #TODO: open db
    run_crawler.crawler_runner(cur_state)


if __name__ == "__main__":
    main()
