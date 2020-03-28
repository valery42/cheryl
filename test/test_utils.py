from cheryl.utils import quote, unquote, get_prompt, cannot_be_empty


def test_quote():
    item = 42
    assert quote(item) == "'42'"


def test_unquote():
    item = "'42'"
    assert unquote(item) == "42"


def test_get_prompt():
    prompt = get_prompt(message="hello", gaps=1)
    assert prompt == "    hello> "


def test_cannot_be_empty():
    assert cannot_be_empty("value", gaps=1) == "    value cannot be empty"
