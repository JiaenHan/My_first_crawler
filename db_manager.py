"""
This module manage the SQLite Database
"""


import sqlite3


class DBmanager:
    """Managing the MySQL database."""
    def __init__(self, starting_url: str):
        """Create or Open the database"""
        self._conn = sqlite3.connect("crawler.db")
        self._cursor = self._conn.cursor()


    def _get_index(self, url: str):
        """Get the index of a url"""

    def add_new_url(self, url: str):
        """Adding new url into database"""

    def add_connection(self, fatherUrl: str, childUrl: str):
        """Adding connections between two urls"""

    def close_db(self):
        """Closing dp connection"""

__all__ = [
    DBmanager.__name__
]
