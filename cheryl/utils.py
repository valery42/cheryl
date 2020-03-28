from cheryl.config import GAP, ARROW


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
