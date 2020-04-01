from random import randrange

try:
    from cheryl.config import MIN_PAGES, MAX_PAGES
except ModuleNotFoundError:
    MIN_PAGES = 1
    MAX_PAGES = 9999


def get_pages_list(n):
    result = [randrange(MIN_PAGES, MAX_PAGES) for _ in range(n)]
    return result
