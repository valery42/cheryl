from cheryl.engine import Engine
from test.helpers import (
    create_database, delete_database,
    get_records, get_books,
)


class TestEngine:
    def test_load_database(self):
        db_name = "test_database"
        create_database(db_name)
        engine = Engine(db_name)
        engine.load_database()
        assert engine.books == get_books()
        delete_database(db_name)
    

    def test_store_database(self):
        db_name = "test_database"
        engine = Engine(db_name)
        engine.books = get_books()
        engine.store_database()
        with open(db_name, "rt") as db:
            records = [record.strip() for record in db]
        assert records == get_records()
        delete_database(db_name)
