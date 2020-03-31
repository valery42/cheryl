"""This module contains various utility functions."""

from cheryl.checkers import is_correct_isbn, is_correct_pages
from cheryl.config import (
    GAP, ARROW, ISBN_PATTERN, MAX_PAGES,
    ISBN_LENGTH, PAGES_LENGTH, SPACE_AROUND,
    FORMAT_STRING,
)


def quote(item: str, *, quote_type: str = "'") -> str:
    """Quote item with quote_type of quotes."""
    return f"{quote_type}{item}{quote_type}"


def unquote(item: str, *, quote_type: str = "'") -> str:
    """Unquote item from quote_type of quotes."""
    return item.strip(quote_type)


def get_sorted_by() -> dict:
    """Get sorted_by Engine attribute."""
    sorted_by = {
        "isbn": False,
        "title": False,
        "author": False,
        "publisher": False,
        "pages": False,
    }
    return sorted_by


def get_longest() -> dict:
    """Get longest Engine attribute."""
    longest = {
        "title": 0,
        "author": 0,
        "publisher": 0,
    }
    return longest


def get_prompt(*, message: str, gaps=0) -> str:
    """Get a new prompt string using given message."""
    return f"{gaps*GAP}{message}{ARROW}"


def get_from_user(*, message: str, gaps=0, lower=True) -> str:
    """Get value from user.

    Set lower to False if needed.
    """
    prompt = get_prompt(message=message, gaps=gaps)
    value = input(prompt)
    value = value.strip()
    if lower:
        return value.lower()
    else:
        return value


def is_correct(value, *, checker=None) -> bool:
    """Check if value is correct using checker function."""
    if checker:
        return checker(value)
    else:
        return bool(value)


def get_book_attr(*, attr: str, error: str, checker=None) -> str:
    """Get book attribute from user.

    checker function is used to check attribute for correctness.
    """
    message = attr
    while True:
        attr = get_from_user(message=message, gaps=1, lower=False)
        if is_correct(attr, checker=checker):
            break
        else:
            print(error)
    return attr


def there_is_nothing_to(do):
    """Inform user that there are no books."""
    print(f"There is nothing to {do} yet")


def key_must_be_in(keys):
    """Inform user that key must be in keys."""
    print(f"Key must be in {keys}")


def cannot_perform_action(action, key, target):
    """Inform user that the program cannot perform action."""
    print(f"Cannot {action} a book with {key} '{target}'")


def get_empty_attr_error(attr, *, gaps=0) -> str:
    """Return empty attribute error."""
    return f"{gaps*GAP}{attr} cannot be empty"


def get_isbn_error(*, gaps=0) -> str:
    """Return isbn error."""
    return f"{gaps*GAP}isbn must be like '{ISBN_PATTERN}' where 'd' is digit"


def get_pages_error(*, gaps=0) -> str:
    """Return pages error."""
    return f"{gaps*GAP}pages must be positive integer less than {MAX_PAGES+1}"


def create_book():
    """Create a new book."""
    book = {}
    book["isbn"] = get_book_attr(attr="isbn", error=get_isbn_error(gaps=2),
                                 checker=is_correct_isbn)
    book["title"] = get_book_attr(attr="title",
                                  error=get_empty_attr_error("title", gaps=2))
    book["author"] = get_book_attr(
        attr="author",
        error=get_empty_attr_error("author", gaps=2))
    book["publisher"] = get_book_attr(
        attr="publisher",
        error=get_empty_attr_error("publisher", gaps=2))
    book["pages"] = int(get_book_attr(attr="pages",
                                      error=get_pages_error(gaps=2),
                                      checker=is_correct_pages))
    return book


def print_book(engine, book):
    """Print book using FORMAT_STRING."""
    print(FORMAT_STRING.format(
        book["isbn"], ISBN_LENGTH + SPACE_AROUND,
        book["title"], engine.longest["title"] + SPACE_AROUND,
        book["author"], engine.longest["author"] + SPACE_AROUND,
        book["publisher"], engine.longest["publisher"] + SPACE_AROUND,
        book["pages"], PAGES_LENGTH + SPACE_AROUND,
    ))


def print_books(engine):
    """Print all books."""
    for book in engine.books:
        print_book(engine, book)
