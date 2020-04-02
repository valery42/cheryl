#!/usr/bin/env python3

"""This module is a top level script to create database of n records."""

import argparse

from cheryl.utils import quote
from cheryl.config import DEFAULT_DATABASE_NAME
from generator.isbn import get_isbn_list
from generator.title import get_title_list
from generator.author import get_author_list
from generator.publisher import get_publisher_list
from generator.pages import get_pages_list

parser = argparse.ArgumentParser()
parser.add_argument("n", help="number of records to generate", type=int)
args = parser.parse_args()


def create_database(n):
    """Create database of n records."""
    isbn = get_isbn_list(n)
    title = get_title_list(n)
    author = get_author_list(n)
    publisher = get_publisher_list(n)
    pages = get_pages_list(n)

    with open(DEFAULT_DATABASE_NAME, "wt") as db:
        for record in zip(isbn, title, author, publisher, pages):
            record = [quote(item) for item in record]
            print(",".join(record), file=db)


create_database(args.n)
