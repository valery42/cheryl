def quote(item, *, quote_type="'"):
    return f"{quote_type}{item}{quote_type}"


def unquote(item, *, quote_type="'"):
    return item.strip(quote_type)
