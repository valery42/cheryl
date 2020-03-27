from cheryl.config import UNSUCCESSFUL


def binary_search(books, *, key, target):
    left = 0
    right = len(books) - 1
    while left <= right:
        middle = (left + right) // 2
        if books[middle][key] < target:
            left = middle + 1
        elif books[middle][key] > target:
            right = middle - 1
        else:
            return middle
    return UNSUCCESSFUL
