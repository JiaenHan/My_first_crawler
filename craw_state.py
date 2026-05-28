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
    
    def has_seen(self, url: str) -> bool:
        """Determine if a url has been seen before"""
        return url in self._seen_url
    
    def add_to_unseen(self, url: str) -> None:
        """Adding new url to unseen"""
        if not self.has_seen(url):
            self._unseen_url.append(url)

    def change_to_seen(self, url: str) -> None:
        """Move an url from unseen to seen"""
        if not self.has_seen(url) and url in self._unseen_url:
            self._unseen_url.remove(url)
            self._seen_url.append(url)


__all__ = [
    CrawState.__name__
]
