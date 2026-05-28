"""
This module is the entrance of the
crawler
"""


from craw_state import CrawState


def main() -> None:
    """The starting point of the program"""
    cur_state = CrawState("https://ics.uci.edu")


if __name__ == "__main__":
    main()