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
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS urls(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL UNIQUE
            ) STRICT;
            """
        )

        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS url_conn(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_id INTEGER NOT NULL,
                child_id INTEGER NOT NULL
            ) STRICT;
            """
        )

        self._conn.commit()
        self.add_new_url(starting_url)

    def _get_index(self, url: str) -> int:
        """Get the index of a url"""
        self._cursor.execute(
            """
            SELECT id
            FROM urls
            WHERE url = ?;
            """, (url, )
        )
        result = self._cursor.fetchone()
        if result is None:
            return None
        return result[0]

    def add_new_url(self, url: str):
        """Adding new url into database"""
        try:
            self._cursor.execute(
                """
                INSERT OR IGNORE INTO urls (url)
                VALUES (?);
                """, (url, )
            )
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            print(f"{e} at add_new_url")

    def add_connection(self, fatherUrl: str, childUrl: str):
        """Adding connections between two urls"""
        try:
            parent_id = self._get_index(fatherUrl)
            child_id = self._get_index(childUrl)
            if not (parent_id is None or child_id is None):
                self._cursor.execute(
                    """
                    INSERT OR IGNORE INTO url_conn (parent_id, child_id)
                    VALUES (?, ?);
                    """, (parent_id, child_id)
                )
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            print(f"{e} at add_connection")

    def close_db(self):
        """Closing dp connection"""
        self._conn.commit()
        self._cursor.close()
        self._conn.close()

__all__ = [
    DBmanager.__name__
]
