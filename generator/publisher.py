from random import choice
from string import ascii_uppercase as UPPER


def get_publisher_list(n):
    result = []
    for _ in range(n):
        publisher = choice(UPPER) + choice(UPPER) + " Press"
        result.append(publisher)
    return result
