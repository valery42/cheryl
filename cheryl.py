#!/usr/bin/env python3

"""This module is a top level Cheryl script to run the program."""

import argparse

from cheryl.engine import Engine
from cheryl.handler import Handler
from cheryl.config import NAME, VERSION, DEFAULT_DATABASE_NAME

parser = argparse.ArgumentParser(
    description=f"{NAME} is a library information system"
)
parser.add_argument(
    "-db", "--database",
    help="database to load records from and store books to"
)
args = parser.parse_args()
args.database = args.database or DEFAULT_DATABASE_NAME


def main():
    """Main function.
    
    Cheryl program starts here."""
    print(f"{NAME} version {VERSION}")
    print("Enter '.help' for usage hints.")
    engine = Engine(args.database)
    handler = Handler(engine)
    handler.handle()


main()
