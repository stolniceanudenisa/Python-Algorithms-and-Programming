from unittest import TestCase
from domain.book_model import Book

class TestBook(TestCase):

    def setUp(self):
        # this function will be run at the beginning of each test method
        self.book = Book("9780261103252", "Lord of the rings", "adventure", 1995, 105.0, 3)

    def test_create(self):
        self.assertEqual(self.book.get_isbn(), "9780261103252")
        self.assertEqual(self.book.get_title(), "Lord of the rings")
        self.assertEqual(self.book.get_genre(), "adventure")
        self.assertEqual(self.book.get_year(), 1995)
        self.assertEqual(self.book.get_price(), 105.0)
        self.assertEqual(self.book.get_quantity(), 3)

        self.assertEqual(str(self.book), "Book(isbn=9780261103252, title=Lord of the rings, genre=adventure, year=1995, price=105.0, quantity=3)")

        # test if error is raised when genre is not from the given values
        self.assertRaises(AttributeError, Book, "", "", "drama", 2020, 50.0, 0)
        # test if error is raised when year is not a proper values
        self.assertRaises(AttributeError, Book, "", "", "sci-fi", 2021, 50.0, 0)
        self.assertRaises(AttributeError, Book, "", "", "sci-fi", 1449, 50.0, 0)
        self.assertRaises(AttributeError, Book, "", "", "sci-fi", -5, 50.0, 0)
        # test if error is raised when price is negative or zero
        self.assertRaises(AttributeError, Book, "", "", "sci-fi", 2020, 0.0, 0)
        self.assertRaises(AttributeError, Book, "", "", "sci-fi", 2020, -10.0, 0)
        # test if error is raised when quantity is negative
        self.assertRaises(AttributeError, Book, "", "", "sci-fi", 2020, 50.0, -10)

        # test setters
        self.assertRaises(AttributeError, self.book.set_genre, "drama")
        # test if error is raised when year is not a proper values
        self.assertRaises(AttributeError, self.book.set_year, 2021)
        self.assertRaises(AttributeError, self.book.set_year, 1449)
        self.assertRaises(AttributeError, self.book.set_year, -5)
        # test if error is raised when price is negative or zero
        self.assertRaises(AttributeError, self.book.set_price, 0.0)
        self.assertRaises(AttributeError, self.book.set_price, -10.0)
        # test if error is raised when quantity is negative
        self.assertRaises(AttributeError, self.book.set_quantity, -10)

        # we check ISBN every time to be sure that it's not changeing
        self.book.set_title("New title")
        self.assertEqual(self.book.get_isbn(), "9780261103252")
        self.assertEqual(self.book.get_title(), "New title")

        self.book.set_genre("sci-fi")
        self.assertEqual(self.book.get_isbn(), "9780261103252")
        self.assertEqual(self.book.get_genre(), "sci-fi")

        self.book.set_year(2012)
        self.assertEqual(self.book.get_isbn(), "9780261103252")
        self.assertEqual(self.book.get_year(), 2012)

        self.book.set_price(50.0)
        self.assertEqual(self.book.get_isbn(), "9780261103252")
        self.assertEqual(self.book.get_price(), 50.0)

        self.book.set_quantity(0)
        self.assertEqual(self.book.get_isbn(), "9780261103252")
        self.assertEqual(self.book.get_quantity(), 0)

        self.assertEqual(str(self.book), "Book(isbn=9780261103252, title=New title, genre=sci-fi, year=2012, price=50.0, quantity=0)")

    def test_equals(self):
        book = Book(self.book.get_isbn(), self.book.get_title(), self.book.get_genre(), self.book.get_year(), self.book.get_price(), self.book.get_quantity())
        self.assertEqual(book, self.book)
        
        book = Book("other isbn", self.book.get_title(), self.book.get_genre(), self.book.get_year(), self.book.get_price(), self.book.get_quantity())
        self.assertNotEqual(book, self.book)
    
        book = Book(self.book.get_isbn(), "New title", self.book.get_genre(), self.book.get_year(), self.book.get_price(), self.book.get_quantity())
        self.assertNotEqual(book, self.book)
        
        book = Book(self.book.get_isbn(), self.book.get_title(), "sci-fi", self.book.get_year(), self.book.get_price(), self.book.get_quantity())
        self.assertNotEqual(book, self.book)
        
        book = Book(self.book.get_isbn(), self.book.get_title(), self.book.get_genre(), 2012, self.book.get_price(), self.book.get_quantity())
        self.assertNotEqual(book, self.book)
        
        book = Book(self.book.get_isbn(), self.book.get_title(), self.book.get_genre(), self.book.get_year(), 50.0, self.book.get_quantity())
        self.assertNotEqual(book, self.book)
        
        book = Book(self.book.get_isbn(), self.book.get_title(), self.book.get_genre(), self.book.get_year(), self.book.get_price(), 0)
        self.assertNotEqual(book, self.book)

    def test_title_contains_word(self):
        self.assertTrue(self.book.title_contains("rings"))
        self.assertTrue(self.book.title_contains("RINGS"))
        self.assertTrue(self.book.title_contains("Rings"))
        self.assertTrue(self.book.title_contains("rINGS"))
        self.assertTrue(self.book.title_contains("lord"))

        self.assertFalse(self.book.title_contains("new"))
        self.assertFalse(self.book.title_contains("NEW"))
        self.assertFalse(self.book.title_contains("New"))
        self.assertFalse(self.book.title_contains("nEW"))

    def test_publicated_between_years(self):
        self.assertTrue(self.book.publicated_between_years(1990, 2000))
        self.assertTrue(self.book.publicated_between_years(1995, 1995))

        self.assertFalse(self.book.publicated_between_years(2000, 1990))
        self.assertFalse(self.book.publicated_between_years(1452, 1990))
        self.assertFalse(self.book.publicated_between_years(2000, 2020))

    def test_is_at_stock(self):
        self.assertTrue(self.book.is_at_stock())
        self.book.set_quantity(0)
        self.assertFalse(self.book.is_at_stock())
        