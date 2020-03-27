from cheryl.converters import record_to_book, book_to_record


class Engine:
    def __init__(self, db_name):
        self.books = []
        self.db_name = db_name
    
    def load_database(self):
        with open(self.db_name, "rt") as db:
            for record in db:
                book = record_to_book(record)
                self.add_book(book)
    
    def store_database(self):
        with open(self.db_name, "wt") as db:
            for book in self.books:
                record = book_to_record(book)
                print(record, file=db)

    def add_book(self, book):
        self.books.append(book)
    
    def delete_book(self, *, index):
        del self.books[index]
    