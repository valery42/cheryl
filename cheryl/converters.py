from cheryl.utils import quote, unquote


def record_to_book(record):
    book = {}
    record = record.strip()
    record = [unquote(value) for value in record.split(",")]
    isbn, title, author, publisher, pages = record
    book["isbn"] = isbn
    book["title"] = title
    book["author"] = author
    book["publisher"] = publisher
    book["pages"] = int(pages)
    return book


def book_to_record(book):
    record = [quote(value) for value in book.values()]
    return ",".join(record)
