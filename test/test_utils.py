from cheryl.utils import quote, unquote, get_prompt


def test_quote():
    item = 42
    assert quote(item) == "'42'"


def test_unquote():
    item = "'42'"
    assert unquote(item) == "42"


def test_get_prompt():
    prompt = get_prompt(message="hello", gaps=1)
    assert prompt == "    hello> "
