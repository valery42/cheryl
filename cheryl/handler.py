"""This module contains a class that handles user commands."""

from cheryl.checkers import is_correct_isbn, is_correct_pages
from cheryl.utils import (
    get_from_user, create_book,
    print_book, print_books,
    there_is_nothing_to, key_must_be_in, cannot_perform_action,
    get_isbn_error, get_pages_error, get_empty_attr_error,
)
from cheryl.config import (
    CHERYL,
    GAP,

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

    COMMAND_TO_DESCRIPTION,
)


class Handler:
    """A class that handles user commands."""

    def __init__(self, engine):
        self.engine = engine
    
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
        elif key == "pages" and not is_correct_pages(target):
            print(get_pages_error())
            return False
        elif not target:
            print(get_empty_attr_error(key))
            return False
        return True
    
    def handle_add(self):
        """Handle Engine add_book operation."""
        book = create_book()
        title = book["title"]
        author = book["author"]
        self.engine.add_book(book)
        print(f"'{title}' by {author} has been successfully added")
    
    def sort_books(self, *, key):
        """handle_sort helper."""
        self.engine.sort_books(key=key)
        print(f"Books have been sorted by {key}")
    
    def handle_sort(self):
        """Handle Engine sort_books operation."""
        continue_ = self.continue_on_condition(self.engine.books, None,
                                               there_is_nothing_to, "sort")
        if continue_:
            key = get_from_user(message="sort by key", gaps=1)
            condition = key in SORT_KEYS
            self.continue_on_condition(condition, self.sort_books,
                                       key_must_be_in, SORT_KEYS, key=key)
    
    def print_books(self):
        """handle_print helper."""
        print_books(self.engine)
    
    def handle_print(self):
        """Handle utils print_books operation."""
        self.continue_on_condition(self.engine.books, self.print_books,
                                   there_is_nothing_to, "print")
    
    def print_book(self, *, index):
        """handle_find helper."""
        print_book(self.engine, self.engine.books[index])
    
    def delete_book(self, *, index):
        """handle_delete helper."""
        book = self.engine.books[index]
        title, author = book["title"], book["author"]
        print(f"'{title}' by {author} has been successfully deleted")
        self.engine.delete_book(index=index)

    def change_book(self, *, index):
        """handle_change helper."""
        key = get_from_user(message="update key", gaps=1)
        condition = key in SORT_KEYS
        continue_ = self.continue_on_condition(condition, None,
                                               key_must_be_in, SORT_KEYS)
        if continue_:
            value = get_from_user(message=f"new {key}", gaps=1, lower=False)
            if self.correct_key_and_target(key, value):
                if key == "pages":
                    value = int(value)
                self.engine.books[index][key] = value
                print(f"{key} has been successfully changed to '{value}'")

    def find_and_perform(self, action, verb):
        """Operation used by handle_find, handle_delete, and handle_change."""
        continue_ = self.continue_on_condition(self.engine.books, None,
                                               there_is_nothing_to, verb)
        if continue_:
            key = get_from_user(message="find by key", gaps=1)
            condition = key in FIND_KEYS
            continue_ = self.continue_on_condition(condition, None,
                                                   key_must_be_in, FIND_KEYS)
            if continue_:
                target = get_from_user(message=f"{key}", gaps=1, lower=False)
                if self.correct_key_and_target(key, target):
                    index = self.engine.find_book(key=key, target=target)
                    condition = index != UNSUCCESSFUL
                    self.continue_on_condition(
                        condition, action, cannot_perform_action,
                        "find", key, target, index=index,
                    )
    
    def handle_find(self):
        """Handle Engine find_book operation."""
        self.find_and_perform(self.print_book, "find")

    def handle_delete(self):
        """Handle Engine delete_book operation."""
        self.find_and_perform(self.delete_book, "delete")
    
    def handle_change(self):
        """Handle change_book operation."""
        self.find_and_perform(self.change_book, "change")
    
    def handle_quit(self):
        """Handle quit operation."""
        self.engine.store_database()
        print("Bye.")
    
    def handle_help(self):
        """Handle help operation."""
        for command, description in COMMAND_TO_DESCRIPTION.items():
            print(f"{GAP}{command:10}{2*GAP}{description}")
    
    def load_database(self):
        self.engine.load_database()

    def handle(self):
        self.load_database()
        
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
            
            elif command in DELETE_SYNONYMS:
                self.handle_delete()
            
            elif command in CHANGE_SYNONYMS:
                self.handle_change()
            
            elif command in HELP_SYNONYMS:
                self.handle_help()

            elif command in QUIT_SYNONYMS:
                self.handle_quit()
                break
            
            else:
                if not command:
                    print(get_empty_attr_error("Command"))
                else:
                    print(f"There is no such command '{command}'. "
                          "Please, try again.")
