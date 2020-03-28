from cheryl.config import (
    MIN_PAGES, MAX_PAGES, ISBN_SEP, ISBN_NUM_VALUES, ISBN_VALUE_LENGTH
)


def is_correct_pages(pages):
    return pages.isnumeric() and MIN_PAGES <= int(pages) <= MAX_PAGES


def is_correct_isbn(isbn):
    values = isbn.split(ISBN_SEP)
    if len(values) != ISBN_NUM_VALUES:
        return False
    for value in values:
        if not value.isnumeric() or len(value) != ISBN_VALUE_LENGTH:
            return False
    return True
