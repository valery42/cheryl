#!/usr/bin/env python3

import argparse

from generator.isbn import get_isbn_list
from generator.title import get_title_list
from generator.author import get_author_list
from generator.publisher import get_publisher_list
from generator.pages import get_pages_list
from cheryl.utils import quote

parser = argparse.ArgumentParser()
parser.add_argument("n", help="number of records to generate", type=int)
args = parser.parse_args()


def create_database(n):
    isbn = get_isbn_list(n)
    title = get_title_list(n)
    author = get_author_list(n)
    publisher = get_publisher_list(n)
    pages = get_pages_list(n)

    with open("my-books.csv", "wt") as db:
        for record in zip(isbn, title, author, publisher, pages):
            record = [quote(item) for item in record]
            print(",".join(record), file=db)


create_database(args.n)
