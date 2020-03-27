from cheryl.converters import record_to_book, book_to_record
from test.helpers import get_record, get_book


def test_record_to_book():
    record = get_record()
    assert record_to_book(record) == get_book()


def test_book_to_record():
    book = get_book()
    assert book_to_record(book) == get_record()
