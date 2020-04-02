"""This module contains publisher generator."""

from random import choice

NAMES = [
    # 25 masculine names
    "Alexander", "Andrew", "Arthur", "Ben", "Brad",
    "Carl", "Chance", "Corey", "Damien", "Derek",
    "Doug", "Duncan", "Earl", "Eddie", "Elliot",
    "Eric", "Felix", "Floyd", "Gary", "Grant",
    "Howard", "Jack", "Jerry", "Kevin", "Ronald",

    # 25 feminine names
    "Amy", "Anne", "Astrid", "Betty", "Carol",
    "Cheryl", "Cleo", "Daisy", "Drew", "Effie",
    "Esty", "Faith", "Glenda", "Helen", "Ivy",
    "Karen", "Katie", "Lauren", "Lina", "Maggie",
    "Nancy", "Rachel", "Vanessa", "Teresa", "Wendy", 
]

SURNAMES = [
    # 50 surnames
    "Amber", "Artley", "Baker", "Bluck", "Buller",
    "Cheever", "Clinton", "Cole", "Cook", "Cox",
    "Dinn", "Duke", "Ellis", "Flann", "Goodburn",
    "Hackett", "Hall", "Haskett", "Irwin", "Jackson",
    "Klayman", "Knight", "Lea", "Lee", "Livings",
    "Lowson", "Maggs", "Meyers", "Neeve", "Osborne",
    "Parker", "Patten", "Perry", "Pierce", "Pitt",
    "Roope", "Rudd", "Simpson", "Smith", "Stone",
    "Sutton", "Taylor-Johnson", "Tomson", "Tutin", "Tyler",
    "Veal", "Waide", "Wilde", "Wright", "Yeabsley",
]


def get_author_list(n):
    """Generate list of n publisher values."""
    author = [choice(NAMES) + " " + choice(SURNAMES) for _ in range(n)]
    return author
