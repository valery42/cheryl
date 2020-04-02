from random import choice
from string import ascii_uppercase as UPPER


def get_publisher_list(n):
    publisher = [choice(UPPER) + choice(UPPER) + " Press" for _ in range(n)]
    return publisher
