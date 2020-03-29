from cheryl.checkers import is_correct_isbn
from cheryl.utils import (
    get_from_user, create_book,
    print_book, print_books,
    there_is_nothing_to, key_must_be_in, cannot_perform_action,
    get_isbn_error, get_empty_attr_error,
)
from cheryl.config import (
    CHERYL,

    SORT_KEYS,
    FIND_KEYS,

    UNSUCCESSFUL,

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
                key_must_be_in(SORT_KEYS)
        else:
            there_is_nothing_to("sort")
    
    def handle_print(self):
        if self.engine.books:
            print_books(self.engine)
        else:
            there_is_nothing_to("print")
    
    def handle_find(self):
        if self.engine.books:
            key = get_from_user(message="by", gaps=1)
            if key in FIND_KEYS:
                target = get_from_user(message=f"{key}", gaps=1, lower=False)
                if key == "isbn" and not is_correct_isbn(target):
                    print(get_isbn_error())
                elif not target:
                    print(get_empty_attr_error(key))
                else:
                    index = self.engine.find_book(key=key, target=target)
                    if index != UNSUCCESSFUL:
                        print_book(self.engine, self.engine.books[index])
                    else:
                        cannot_perform_action("find", key, target)
            else:
                key_must_be_in(FIND_KEYS)
        else:
            there_is_nothing_to("find")
    
    def handle_quit(self):
            self.engine.store_database()
            print("Bye.")
    
    def handle(self):
        while True:
            command = get_from_user(message=CHERYL)

            if command in ADD_SYNONYMS:
                self.handle_add()
            
            elif command in SORT_SYNONYMS:
                self.handle_sort()
            
            elif command in PRINT_SYNONYMS:
                self.handle_print()
            
            elif command in FIND_SYNONYMS:
                self.handle_find()
            
            elif command in QUIT_SYNONYMS:
                self.handle_quit()
                break
            
            else:
                if not command:
                    print(get_empty_attr_error("Command"))
                else:
                    print(f"There is no such command '{command}'. "
                          "Please, try again.")
