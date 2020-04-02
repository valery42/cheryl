"""This module contains a class to test heapsort algorithm implementation."""

from cheryl.sort import heapsort
from test.helpers import get_book, get_books


class TestHeapSort:
    """A class to test heapsort algorithm implementation."""
    
    def test_empty_list(self):
        books = []
        heapsort(books, key="key")
        assert books == []
    
    def test_one_element_list_string_key(self):
        books = [get_book()]
        heapsort(books, key="publisher")
        assert books == [get_book()]

    def test_one_element_list_int_key(self):
        books = [get_book()]
        heapsort(books, key="pages")
        assert books == [get_book()]

    def test_multi_element_list_string_key(self):
        books = get_books()
        heapsort(books, key="title")
        assert books == sorted(get_books(), key=lambda book: book["title"])
    
    def test_multi_element_list_int_key(self):
        books = get_books()
        heapsort(books, key="pages")
        assert books == sorted(get_books(), key=lambda book: book["pages"])
