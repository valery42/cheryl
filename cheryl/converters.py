"""This module contains converters for records and books."""

from cheryl.utils import quote, unquote


def record_to_book(record: str) -> dict:
    """Convert record to book."""
    book = {}
    record = record.strip()
    record = [unquote(value) for value in record.split("','")]
    isbn, title, author, publisher, pages = record
    book["isbn"] = isbn
    book["title"] = title
    book["author"] = author
    book["publisher"] = publisher
    book["pages"] = int(pages)
    return book


def book_to_record(book: dict) -> str:
    """Convert book to record."""
    record = [quote(value) for value in book.values()]
    return ",".join(record)
