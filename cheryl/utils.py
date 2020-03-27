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
