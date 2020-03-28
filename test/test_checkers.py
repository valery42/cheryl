from cheryl.checkers import (
    is_correct_isbn,
    is_correct_pages,
)


class TestIsCorrectISBN:
    def test_empty_isbn(self):
        isbn = ""
        assert is_correct_isbn(isbn) == False
    
    def test_incorrect_isbn(self):
        isbn = "123-hey-hey"
        assert is_correct_isbn(isbn) == False
    
    def test_too_long_isbn(self):
        isbn = "000-111-222-333"
        assert is_correct_isbn(isbn) == False
    
    def test_correct_isbn(self):
        isbn = "000-111-222"
        assert is_correct_isbn(isbn) == True


class TestIsCorrectPages:
    def test_empty_pages(self):
        pages = ""
        assert is_correct_pages(pages) == False

    def test_incorrect_pages(self):
        pages = "forty two"
        assert is_correct_pages(pages) == False

    def test_too_few_pages(self):
        pages = "0"
        assert is_correct_pages(pages) == False

    def test_too_many_pages(self):
        pages = "10000"
        assert is_correct_pages(pages) == False

    def test_correct_pages(self):
        pages = "42"
        assert is_correct_pages(pages) == True
