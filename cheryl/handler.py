from cheryl.utils import get_from_user, create_book
from cheryl.config import (
    CHERYL,

    SORT_KEYS,

    ADD_SYNONYMS,
    HELP_SYNONYMS,
    SORT_SYNONYMS,
    PRINT_SYNONYMS,
    FIND_SYNONYMS,
    DELETE_SYNONYMS,
    CHANGE_SYNONYMS,
    QUIT_SYNONYMS,
)


class Handler:
    def __init__(self, engine):
        self.engine = engine
    
    def handle_add(self):
        book = create_book()
        title = book["title"]
        author = book["author"]
        self.engine.add_book(book)
        print(f"'{title}' by {author} has been successfully added")
    
    def handle_sort(self):
        if self.engine.books:
            key = get_from_user(message="by", gaps=1)
            if key in SORT_KEYS:
                self.engine.sort_books(key=key)
                print(f"Books have been sorted by {key}")
            else:
                print(f"Undefined key '{key}'. Key must be in {SORT_KEYS}")
        else:
            print("There is nothing to sort yet")
    
    def handle_quit(self):
            self.engine.store_database()
            print("Bye.")
    
    def handle(self):
        while True:
            command = get_from_user(message=CHERYL)
            command = command.lower()

            if command in ADD_SYNONYMS:
                self.handle_add()
            
            elif command in SORT_SYNONYMS:
                self.handle_sort()
            
            elif command in QUIT_SYNONYMS:
                self.handle_quit()
                break
            
            else:
                print(f"There is no such command '{command}'. "
                      "Please, try again.")
