"""
This module contains a class that organize
the state of the crawler
"""

from collections import deque


class CrawState:
    """Abstract the state of the crawler"""
    def __init__(self, start: str):
        """Initialize a CrawState"""
        self._start = start
        self._wait_queue = deque()
        self._wait_queue.appendleft(start)
        self._seen_url = set()
        self._unseen_url = set()
        self._unseen_url.add(start)

    def get_start(self) -> str:
        """Obtain the starting point of the crawler"""
        return self._start
    
    def still_has_unseen(self) -> bool:
        """Determine if there's still content unseen"""
        return len(self._unseen_url) > 0
    
    def pop_unseen_url(self) -> str:
        """Get the first unseen url in the list"""
        url = self._wait_queue.popleft()
        self._unseen_url.remove(url)
        self._seen_url.add(url)
        return url
    
    def has_seen(self, url: str) -> bool:
        """Determine if a url has been seen before"""
        return url in self._seen_url
    
    def add_to_unseen(self, url: str) -> None:
        """Adding new url to unseen"""
        if not self.has_seen(url) and url in self._unseen_url:
            self._unseen_url.add(url)
            self._wait_queue.appendleft(url)
            
    '''
    def change_to_seen(self, url: str) -> None:
        """Move an url from unseen to seen"""
        if not self.has_seen(url) and url in self._unseen_url:
            self._unseen_url.remove(url)
            self._seen_url.append(url)
    '''


__all__ = [
    CrawState.__name__
]
