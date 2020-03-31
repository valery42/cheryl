UNSUCCESSFUL = -1

MIN_PAGES = 1
MAX_PAGES = 9999

ISBN_PATTERN = "ddd-ddd-ddd"
ISBN_SEP = "-"
ISBN_NUM_VALUES = 3
ISBN_VALUE_LENGTH = 3

ISBN_LENGTH = len(ISBN_PATTERN)
PAGES_LENGTH = len(str(MAX_PAGES))
SPACE_AROUND = 2

GAP = 4 * " "
ARROW = "> "
CHERYL = "cheryl"

FORMAT_STRING = "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|"

SORT_KEYS = ("isbn", "title", "author", "publisher", "pages")
FIND_KEYS = ("isbn", "title")

ADD_SYNONYMS = ("add", "create", "new")
HELP_SYNONYMS = (".help", "help")
SORT_SYNONYMS = ("sort", "order")
PRINT_SYNONYMS = ("print", "display", "list")
FIND_SYNONYMS = ("find", "search", "get")
DELETE_SYNONYMS = ("delete", "del", "remove", "rm")
CHANGE_SYNONYMS = ("change", "update", "set")
QUIT_SYNONYMS = ("quit", "exit")

COMMAND_TO_DESCRIPTION = {
    "print": "Print stored books",
    "sort": "Sort books by key",
    "find": "Find a book by key",
    "add": "Add a new book",
    "delete": "Delete a book by key",
    "change": "Change book attribute by key",
    "quit": "Exit program",
    "help": "Print information about commands",
}

NAME = "Cheryl"
VERSION = "0.1"
