from cheryl.config import GAP, ARROW, ISBN_PATTERN, MAX_PAGES
from cheryl.checkers import is_correct_isbn, is_correct_pages


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


def get_book_attr(*, attr, error, checker=None):
    message = attr
    while True:
        attr = get_from_user(message=message, gaps=1)
        if checker:
            if checker(attr):
                break
        else:
            if attr:
                break
        print(error)
    return attr


def cannot_be_empty(attr, *, gaps=2):
    return f"{gaps*GAP}{attr} cannot be empty"


def create_book():
    book = {}
    isbn = get_book_attr(
        attr="isbn",
        error=f"{2*GAP}isbn must be like '{ISBN_PATTERN}' where 'd' is digit",
        checker=is_correct_isbn,
    )
    title = get_book_attr(attr="title", error=cannot_be_empty("title"))
    author = get_book_attr(attr="author", error=cannot_be_empty("author"))
    publisher = get_book_attr(attr="publisher",
                              error=cannot_be_empty("publisher"))
    pages = get_book_attr(
        attr="pages",
        error=f"{2*GAP}pages must be positive integer less than {MAX_PAGES+1}",
        checker=is_correct_pages,
    )
    book["isbn"] = isbn
    book["title"] = title
    book["author"] = author
    book["publisher"] = publisher
    book["pages"] = int(pages)
    return book
