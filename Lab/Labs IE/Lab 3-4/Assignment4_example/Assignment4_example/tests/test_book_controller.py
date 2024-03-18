from unittest import TestCase

from domain.book_model import Book
from infrastructure.book_repository import BookRepository
from application.controller import BookController

class TestBookController(TestCase):

    def setUp(self):
        self.empty_controller = BookController(BookRepository())
        self.book_controller = BookController(BookRepository([Book("9780552779777", "The girl on the train", "romance", 2016, 61.0, 1)]))
        self.lor_controller = BookController(BookRepository([
            Book("9780261102354", "Lord of the rings - The fellowship of the ring", "adventure", 1991, 40.0, 0),
            Book("9780261102361", "Lord of the rings - The two towers", "adventure", 2007, 39.0, 5),
            Book("9780261102378", "Lord of the rings - The return of the king", "adventure", 2007, 39.0, 2)
        ]))
        self.hobbit = Book("9780261102217", "The hobbit", "adventure", 2006, 44.0, 9)

    def test_create(self):
        self.assertEqual(len(self.empty_controller.get_content()), 0)
        self.assertEqual(len(self.book_controller.get_content()), 1)
        self.assertEqual(len(self.lor_controller.get_content()), 3)

        self.assertEqual(str(self.empty_controller), "[]")
        self.assertEqual(str(self.book_controller), "['Book(isbn=9780552779777, title=The girl on the train, genre=romance, year=2016, price=61.0, quantity=1)']")
        self.assertEqual(str(self.lor_controller), "['Book(isbn=9780261102354, title=Lord of the rings - The fellowship of the ring, genre=adventure, year=1991, price=40.0, quantity=0)', 'Book(isbn=9780261102361, title=Lord of the rings - The two towers, genre=adventure, year=2007, price=39.0, quantity=5)', 'Book(isbn=9780261102378, title=Lord of the rings - The return of the king, genre=adventure, year=2007, price=39.0, quantity=2)']")
        
    def test_get_index(self):
        for index in range(-5, 6):
            self.assertRaises(IndexError, self.empty_controller.get_index, index)
        for index in range(-5, 0):
            self.assertRaises(IndexError, self.book_controller.get_index, index)
            self.assertRaises(IndexError, self.lor_controller.get_index, index)
        for index in range(1, 100):
            self.assertRaises(IndexError, self.book_controller.get_index, index)
        for index in range(3, 100):
            self.assertRaises(IndexError, self.lor_controller.get_index, index)

        res = self.book_controller.get_index(0)
        self.assertEqual(res.get_isbn(), "9780552779777")
        self.assertEqual(res.get_title(), "The girl on the train")
        self.assertEqual(res.get_genre(), "romance")
        self.assertEqual(res.get_year(), 2016)
        self.assertEqual(res.get_price(), 61.0)
        self.assertEqual(res.get_quantity(), 1)

        res = self.lor_controller.get_index(1)
        self.assertEqual(res.get_isbn(), "9780261102361")
        self.assertEqual(res.get_title(), "Lord of the rings - The two towers")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2007)
        self.assertEqual(res.get_price(), 39.0)
        self.assertEqual(res.get_quantity(), 5)

    def test_get_isbn(self):
        self.assertRaises(IndexError, self.empty_controller.get_isbn, "9780261102361")
        self.assertRaises(IndexError, self.empty_controller.get_isbn, "9780552779777")

        self.assertRaises(IndexError, self.book_controller.get_isbn, "9780261102361")
        self.assertRaises(IndexError, self.lor_controller.get_isbn, "9780552779777")

        res = self.book_controller.get_isbn("9780552779777")
        self.assertEqual(res.get_title(), "The girl on the train")
        self.assertEqual(res.get_genre(), "romance")
        self.assertEqual(res.get_year(), 2016)
        self.assertEqual(res.get_price(), 61.0)
        self.assertEqual(res.get_quantity(), 1)

        res = self.lor_controller.get_isbn("9780261102361")
        self.assertEqual(res.get_title(), "Lord of the rings - The two towers")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2007)
        self.assertEqual(res.get_price(), 39.0)
        self.assertEqual(res.get_quantity(), 5)

    def test_get_books_with_genre(self):
        self.assertEqual(self.empty_controller.get_repo(), self.empty_controller.get_books_with_genre("any genre"))

        self.assertEqual(len(self.book_controller.get_books_with_genre("adventure")), 0)
        self.assertEqual(len(self.book_controller.get_books_with_genre("romance")), 1)
        self.book_controller.add_book(self.hobbit)
        self.assertEqual(len(self.book_controller.get_books_with_genre("adventure")), 1)

        self.assertEqual(len(self.lor_controller.get_books_with_genre("adventure")), 3)
        self.assertEqual(len(self.lor_controller.get_books_with_genre("romance")), 0)

    def test_get_available_books(self):
        self.assertEqual(self.empty_controller.get_repo(), self.empty_controller.get_available_books())

        self.assertEqual(len(self.book_controller.get_available_books()), 1)
        self.assertEqual(len(self.lor_controller.get_available_books()), 2)
        self.lor_controller.add_book(self.hobbit)
        self.assertEqual(len(self.lor_controller.get_available_books()), 3)

    def test_add_book(self):
        self.assertEqual(len(self.empty_controller.get_content()), 0)
        self.empty_controller.add_book(self.hobbit)
        self.assertEqual(len(self.empty_controller.get_content()), 1)
        res = self.empty_controller.get_index(0)
        self.assertEqual(res.get_isbn(), "9780261102217")
        self.assertEqual(res.get_title(), "The hobbit")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2006)
        self.assertEqual(res.get_price(), 44.0)
        self.assertEqual(res.get_quantity(), 9)
        self.assertRaises(IndexError, self.empty_controller.add_book, self.hobbit)

    def test_add_new_book(self):
        self.assertEqual(len(self.empty_controller.get_content()), 0)
        self.empty_controller.add_new_book(self.hobbit.get_isbn(), self.hobbit.get_title(), self.hobbit.get_genre(), self.hobbit.get_year(), self.hobbit.get_price(), self.hobbit.get_quantity())
        self.assertEqual(len(self.empty_controller.get_content()), 1)
        res = self.empty_controller.get_index(0)
        self.assertEqual(res.get_isbn(), "9780261102217")
        self.assertEqual(res.get_title(), "The hobbit")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2006)
        self.assertEqual(res.get_price(), 44.0)
        self.assertEqual(res.get_quantity(), 9)
        self.assertRaises(IndexError, self.empty_controller.add_new_book, self.hobbit.get_isbn(), self.hobbit.get_title(), self.hobbit.get_genre(), self.hobbit.get_year(), self.hobbit.get_price(), self.hobbit.get_quantity())

    def test_update_index(self):
        for index in range(-5, 6):
            self.assertRaises(IndexError, self.empty_controller.update_index, index, "", "", 2000, 10.0, 0)
        for index in range(-5, 0):
            self.assertRaises(IndexError, self.book_controller.update_index, index, "", "", 2000, 10.0, 0)
            self.assertRaises(IndexError, self.lor_controller.update_index, index, "", "", 2000, 10.0, 0)
        for index in range(1, 100):
            self.assertRaises(IndexError, self.book_controller.update_index, index, "", "", 2000, 10.0, 0)
        for index in range(3, 100):
            self.assertRaises(IndexError, self.lor_controller.update_index, index, "", "", 2000, 10.0, 0)

        self.book_controller.update_index(0, self.hobbit.get_title(), self.hobbit.get_genre(), self.hobbit.get_year(), self.hobbit.get_price(), self.hobbit.get_quantity())
        res = self.book_controller.get_index(0)
        self.assertEqual(res.get_isbn(), "9780552779777")
        self.assertEqual(res.get_title(), "The hobbit")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2006)
        self.assertEqual(res.get_price(), 44.0)
        self.assertEqual(res.get_quantity(), 9)

        self.lor_controller.update_index(1, self.hobbit.get_title(), self.hobbit.get_genre(), self.hobbit.get_year(), self.hobbit.get_price(), self.hobbit.get_quantity())
        res = self.lor_controller.get_index(1)
        self.assertEqual(res.get_isbn(), "9780261102361")
        self.assertEqual(res.get_title(), "The hobbit")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2006)
        self.assertEqual(res.get_price(), 44.0)
        self.assertEqual(res.get_quantity(), 9)

    def test_update_isbn(self):
        self.assertRaises(IndexError, self.empty_controller.update_isbn, "9780261102361", "", "", 2000, 10.0, 0)
        self.assertRaises(IndexError, self.empty_controller.update_isbn, "9780552779777", "", "", 2000, 10.0, 0)

        self.assertRaises(IndexError, self.book_controller.update_isbn, "9780261102361", "", "", 2000, 10.0, 0)
        self.assertRaises(IndexError, self.lor_controller.update_isbn, "9780552779777", "", "", 2000, 10.0, 0)

        self.book_controller.update_isbn("9780552779777", self.hobbit.get_title(), self.hobbit.get_genre(), self.hobbit.get_year(), self.hobbit.get_price(), self.hobbit.get_quantity())
        res = self.book_controller.get_isbn("9780552779777")
        self.assertEqual(res.get_title(), "The hobbit")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2006)
        self.assertEqual(res.get_price(), 44.0)
        self.assertEqual(res.get_quantity(), 9)

        self.lor_controller.update_isbn("9780261102361", self.hobbit.get_title(), self.hobbit.get_genre(), self.hobbit.get_year(), self.hobbit.get_price(), self.hobbit.get_quantity())
        res = self.lor_controller.get_isbn("9780261102361")
        self.assertEqual(res.get_title(), "The hobbit")
        self.assertEqual(res.get_genre(), "adventure")
        self.assertEqual(res.get_year(), 2006)
        self.assertEqual(res.get_price(), 44.0)
        self.assertEqual(res.get_quantity(), 9)

    def test_update_books_with_genre(self):
        old_value = self.empty_controller
        self.empty_controller.update_books_with_genre("adventure", 1)
        self.assertEqual(self.empty_controller, old_value)

        self.book_controller.update_books_with_genre("romance", 5)
        self.assertEqual(self.book_controller.get_index(0).get_isbn(), "9780552779777")
        self.assertEqual(self.book_controller.get_index(0).get_quantity(), 5)

        self.book_controller.add_book(self.hobbit)
        self.book_controller.update_books_with_genre("adventure", 0)
        self.assertEqual(self.book_controller.get_index(0).get_isbn(), "9780552779777")
        self.assertEqual(self.book_controller.get_index(0).get_quantity(), 5)
        self.assertEqual(self.book_controller.get_index(1).get_isbn(), "9780261102217")
        self.assertEqual(self.book_controller.get_index(1).get_quantity(), 0)

    def test_delete_index(self):
        for index in range(-5, 6):
            self.assertRaises(IndexError, self.empty_controller.delete_index, index)
        for index in range(-5, 0):
            self.assertRaises(IndexError, self.book_controller.delete_index, index)
            self.assertRaises(IndexError, self.lor_controller.delete_index, index)
        for index in range(1, 100):
            self.assertRaises(IndexError, self.book_controller.delete_index, index)
        for index in range(3, 100):
            self.assertRaises(IndexError, self.lor_controller.delete_index, index)
        
        isbn = self.book_controller.get_index(0).get_isbn()
        self.book_controller.delete_index(0)
        for book in self.book_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())

        isbn = self.lor_controller.get_index(1).get_isbn()
        self.lor_controller.delete_index(1)
        for book in self.lor_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())
            
        isbn = self.lor_controller.get_index(1).get_isbn()
        self.lor_controller.delete_index(1)
        for book in self.lor_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())

    def test_delete_isbn(self):
        self.assertRaises(IndexError, self.empty_controller.delete_isbn, "9780261102361")
        self.assertRaises(IndexError, self.empty_controller.delete_isbn, "9780552779777")

        self.assertRaises(IndexError, self.book_controller.delete_isbn, "9780261102361")
        self.assertRaises(IndexError, self.lor_controller.delete_isbn, "9780552779777")

        isbn = "9780552779777"
        self.book_controller.delete_isbn(isbn)
        for book in self.book_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())

        isbn = "9780261102378"
        self.lor_controller.delete_isbn(isbn)
        for book in self.lor_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())

        isbn = "9780261102361"
        self.lor_controller.delete_isbn(isbn)
        for book in self.lor_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())

    def test_delete_not_available_books(self):
        old_value = self.empty_controller
        self.empty_controller.delete_not_available_books()
        self.assertEqual(self.empty_controller, old_value)

        old_value = self.book_controller
        self.book_controller.delete_not_available_books()
        self.assertEqual(self.book_controller, old_value)

        old_value = self.lor_controller
        self.lor_controller.delete_not_available_books()
        self.assertEqual(len(self.lor_controller.get_content()), 2)
        isbn = "9780261102354"
        for book in self.lor_controller.get_content():
            self.assertNotEqual(isbn, book.get_isbn())
        self.assertEqual(self.lor_controller.get_index(0).get_isbn(), "9780261102361")
