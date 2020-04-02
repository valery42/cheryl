"""This module contains pages generator."""

from random import randrange

MIN_PAGES = 50
MAX_PAGES = 1000


def get_pages_list(n):
    """Generate list of n pages values."""
    pages = [randrange(MIN_PAGES, MAX_PAGES) for _ in range(n)]
    return pages
