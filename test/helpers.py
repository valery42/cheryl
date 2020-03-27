import os

from cheryl.converters import record_to_book


def get_record():
    record = "'111-222-333','Martin Eden','Jack London','Penguin','555'"
    return record


def get_book():
    book = {
        "isbn": "111-222-333",
        "title": "Martin Eden",
        "author": "Jack London",
        "publisher": "Penguin",
        "pages": 555,
    }
    return book


def get_records():
    records = [
        "'111-222-333','Martin Eden','Jack London','Penguin','555'",
        "'333-111-222','Catch-22','Joseph Heller','Pilot','777'",
        "'222-333-111','Fight Club','Chuck Palahniuk','Paper Street','333'",
    ]
    return records


def get_books():
    books = [record_to_book(record) for record in get_records()]
    return books


def create_database(db_name):
    records = get_records()
    with open(db_name, "wt") as db:
        for record in records:
            print(record, file=db)


def delete_database(db_name):
    os.remove(db_name)
