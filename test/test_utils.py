from cheryl.utils import quote, unquote


def test_quote():
    item = 42
    assert quote(item) == "'42'"


def test_unquote():
    item = "'42'"
    assert unquote(item) == "42"
