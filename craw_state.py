"""
This module contains a class that organize
the state of the crawler
"""


class CrawState:
    """Abstract the state of the crawler"""
    def __init__(self, start: str):
        """Initialize a CrawState"""
        self._start = start
        self._seen_url = []
        self._unseen_url = [start]

    def get_start(self) -> str:
        """Obtain the starting point of the """
        return self._start
