import io
from contextlib import redirect_stdout

from cheryl.engine import Engine
from test.helpers import get_book
from cheryl.utils import (
    quote, unquote,
    get_prompt, get_empty_attr_error,
    print_book,
)


def test_quote():
    item = 42
    assert quote(item) == "'42'"


def test_unquote():
    item = "'42'"
    assert unquote(item) == "42"


def test_get_prompt():
    prompt = get_prompt(message="hello", gaps=1)
    assert prompt == "    hello> "


def test_get_empty_attr_error():
    assert get_empty_attr_error("value", gaps=1) == "    value cannot be empty"


def test_print_book():
    engine = Engine("")
    book = get_book()
    attrs = [" " + str(attr) + " " for attr in book.values()]
    engine.add_book(book)
    with io.StringIO() as handle:
        with redirect_stdout(handle):
            print_book(engine, book)
            assert handle.getvalue() == "|" + "|".join(attrs) + " |\n"
