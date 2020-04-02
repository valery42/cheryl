from itertools import product

from cheryl.config import ISBN_SEP

DIGITS = [str(i) for i in range(10)]
ISBN_LIMIT = 1_000_000_000
ISBN_DEFAULT_VALUE = ("000",)


def get_isbn_values(n, first, second, third, *, sep=""):
    values = []
    for value in product(first, second, third):
        values.append(sep.join(value))
        if len(values) == n:
            break
    return values


def get_isbn_list(n):
    error_msg = f"n must be positive integer less than {ISBN_LIMIT}"
    assert n > 0 and n <= ISBN_LIMIT, error_msg
    if n <= 1_000:
        first = second = ISBN_DEFAULT_VALUE
        third = get_isbn_values(n, DIGITS, DIGITS, DIGITS)
    elif n <= 1_000_000:
        first = ISBN_DEFAULT_VALUE
        second = third = get_isbn_values(n, DIGITS, DIGITS, DIGITS)
    elif n <= ISBN_LIMIT:
        first = second = third = get_isbn_values(n, DIGITS, DIGITS, DIGITS)
    result = get_isbn_values(n, first, second, third, sep=ISBN_SEP)
    return result
