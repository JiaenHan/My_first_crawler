"""
This module contains the main crawler
"""


import urllib.request
import urllib.error


def open_url(url: str) -> str:
    """Extract data from url"""
    response = None
    try:
        response = urllib.request.urlopen(url)
        content = response.read()
        content = content.decode(encoding = 'utf-8')
        response.close()
        return content
    except (urllib.error.HTTPError, urllib.error.URLError):
        if not response:
            response.close()
        return ""
