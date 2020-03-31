"""This module contains binary search algorithm implementation."""

from cheryl.config import UNSUCCESSFUL


def binary_search(books, *, key, target):
    """Binary search algorithm implementation for books.
    
    key must be either isbn or title.
    """
    target = target.lower()
    left = 0
    right = len(books) - 1
    while left <= right:
        middle = (left + right) // 2
        if books[middle][key].lower() < target:
            left = middle + 1
        elif books[middle][key].lower() > target:
            right = middle - 1
        else:
            return middle
    return UNSUCCESSFUL
