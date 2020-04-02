"""This module contains a class to test binary search implementation."""

from cheryl.config import UNSUCCESSFUL
from cheryl.search import binary_search
from test.helpers import get_book, get_books


class TestBinarySearch:
    """A class to test binary search algorithm implementation."""
    
    def test_empty_list(self):
        assert binary_search([], key="key", target="target") == UNSUCCESSFUL
    
    def test_one_element_list(self):
        books = [get_book()]
        assert binary_search(books, key="title", target="Martin Eden") == 0
    
    def test_multi_element_list(self):
        books = get_books()
        books.sort(key=lambda book: book["isbn"])
        assert binary_search(books, key="isbn", target="333-111-222") == 2
