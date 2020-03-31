from cheryl.checkers import is_correct_isbn, is_correct_pages
from cheryl.config import (
    GAP, ARROW, ISBN_PATTERN, MAX_PAGES,
    ISBN_LENGTH, PAGES_LENGTH, SPACE_AROUND,
)


def quote(item, *, quote_type="'"):
    return f"{quote_type}{item}{quote_type}"


def unquote(item, *, quote_type="'"):
    return item.strip(quote_type)


def get_sorted_by():
    sorted_by = {
        "isbn": False,
        "title": False,
        "author": False,
        "publisher": False,
        "pages": False,
    }
    return sorted_by


def get_longest():
    longest = {
        "title": 0,
        "author": 0,
        "publisher": 0,
    }
    return longest


def get_prompt(*, message, gaps=0):
    return f"{gaps*GAP}{message}{ARROW}"


def get_from_user(*, message, gaps=0, lower=True):
    prompt = get_prompt(message=message, gaps=gaps)
    value = input(prompt)
    value = value.strip()
    if lower:
        return value.lower()
    else:
        return value


def is_correct(value, *, checker=None):
    if checker:
        return checker(value)
    else:
        return bool(value)


def get_book_attr(*, attr, error, checker=None):
    message = attr
    while True:
        attr = get_from_user(message=message, gaps=1, lower=False)
        if is_correct(attr, checker=checker):
            break
        else:
            print(error)
    return attr


def there_is_nothing_to(do):
    print(f"There is nothing to {do} yet")


def key_must_be_in(keys):
    print(f"Key must be in {keys}")


def cannot_perform_action(action, key, target):
    print(f"Cannot {action} a book with {key} '{target}'")


def get_empty_attr_error(attr, *, gaps=0):
    return f"{gaps*GAP}{attr} cannot be empty"


def get_isbn_error(*, gaps=0):
    return f"{gaps*GAP}isbn must be like '{ISBN_PATTERN}' where 'd' is digit"


def get_pages_error(*, gaps=0):
    return f"{gaps*GAP}pages must be positive integer less than {MAX_PAGES+1}"


def create_book():
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


def get_format_string():
    format_string = "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|"
    return format_string


def print_book(engine, book):
    format_string = get_format_string()
    print(format_string.format(
        book["isbn"], ISBN_LENGTH + SPACE_AROUND,
        book["title"], engine.longest["title"] + SPACE_AROUND,
        book["author"], engine.longest["author"] + SPACE_AROUND,
        book["publisher"], engine.longest["publisher"] + SPACE_AROUND,
        book["pages"], PAGES_LENGTH + SPACE_AROUND,
    ))


def print_books(engine):
    for book in engine.books:
        print_book(engine, book)
