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
        book, title, author = create_book()
        self.engine.add_book(book)
        print(f"'{title}' by {author} has been successfully added")
    
    def sort_books(self, *, key):
        self.engine.sort_books(key=key)
        print(f"Books have been sorted by {key}")
    
    def handle_sort(self):
        continue_ = self.continue_on_condition(self.engine.books, None,
                                               there_is_nothing_to, "sort")
        if continue_:
            key = get_from_user(message="by", gaps=1)
            condition = key in SORT_KEYS
            self.continue_on_condition(condition, self.sort_books,
                                       key_must_be_in, SORT_KEYS, key=key)
    
    def print_books(self):
        print_books(self.engine)
    
    def handle_print(self):
        self.continue_on_condition(self.engine.books, self.print_books,
                                   there_is_nothing_to, "print")
       
    def continue_on_condition(self, condition, action, error, *args, **kwargs):
        if condition:
            if action:
                action(**kwargs)
            return True
        else:
            error(*args)
            return False
    
    def correct_key_and_target(self, key, target):
        if key == "isbn" and not is_correct_isbn(target):
            print(get_isbn_error())
            return False
        elif not target:
            print(get_empty_attr_error(key))
            return False
        return True

    def print_book(self, *, index):
        print_book(self.engine, self.engine.books[index])
    
    def handle_find(self):
        continue_ = self.continue_on_condition(self.engine.books, None,
                                               there_is_nothing_to, "find")
        if continue_:
            key = get_from_user(message="by", gaps=1)
            condition = key in FIND_KEYS
            continue_ = self.continue_on_condition(condition, None,
                                                   key_must_be_in, FIND_KEYS)
            if continue_:
                target = get_from_user(message=f"{key}", gaps=1, lower=False)
                if self.correct_key_and_target(key, target):
                    index = self.engine.find_book(key=key, target=target)
                    condition = index != UNSUCCESSFUL
                    self.continue_on_condition(
                        condition, self.print_book, cannot_perform_action,
                        "find", key, target, index=index,
                    )
    
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
