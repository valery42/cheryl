"""This module contains a class to test Engine class."""

from cheryl.engine import Engine
from test.helpers import (
    create_database, delete_database,
    get_records, get_books, get_book,
)


class TestEngine:
    """A class to test Engine class."""
    
    def test_load_database(self):
        db_name = "test_database"
        create_database(db_name)
        engine = Engine(db_name)
        engine.load_database()
        assert engine.books == get_books()
        delete_database(db_name)
    
    def test_store_database(self):
        db_name = "test_database"
        engine = Engine(db_name)
        engine.books = get_books()
        engine.store_database()
        with open(db_name, "rt") as db:
            records = [record.strip() for record in db]
        assert records == get_records()
        delete_database(db_name)
    
    def test_sort_books(self):
        engine = Engine("")
        engine.books = get_books()
        engine.sort_books(key="pages")
        assert engine.books == sorted(get_books(), key=lambda book: book["pages"])
        assert engine.sorted_by["pages"] == True
    
    def test_find_book(self):
        engine = Engine("")
        engine.books = get_books()
        index = engine.find_book(key="isbn", target="222-333-111")
        assert index == 1
    
    def test_update_longest(self):
        engine = Engine("")
        book = get_book()
        engine.add_book(book)
        assert engine.longest == {
            "title": len(book["title"]),
            "author": len(book["author"]),
            "publisher": len(book["publisher"]),
        }
