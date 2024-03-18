from unittest import TestCase

from infrastructure.book_repository import BookRepository
from domain.book_model import Book

class TestBookRepository(TestCase):
    '''
    Test the constructor, the getter and setter methods. Test other functionalities in the controller
    '''

    def setUp(self):
        self.empty_repository = BookRepository()
        self.book_repository = BookRepository([Book("9780552779777", "The girl on the train", "romance", 2016, 61.0, 1)])
        self.lor_repository = BookRepository([
            Book("9780261102354", "Lord of the rings - The fellowship of the ring", "adventure", 1991, 40.0, 0),
            Book("9780261102361", "Lord of the rings - The two towers", "adventure", 2007, 39.0, 5),
            Book("9780261102378", "Lord of the rings - The return of the king", "adventure", 2007, 39.0, 2)
        ])

    def test_create(self):
        self.assertEqual(self.empty_repository.get_list(), [])

        self.assertEqual(str(self.empty_repository), "[]")
        self.assertEqual(str(self.book_repository), "['Book(isbn=9780552779777, title=The girl on the train, genre=romance, year=2016, price=61.0, quantity=1)']")
        self.assertEqual(str(self.lor_repository), "['Book(isbn=9780261102354, title=Lord of the rings - The fellowship of the ring, genre=adventure, year=1991, price=40.0, quantity=0)', 'Book(isbn=9780261102361, title=Lord of the rings - The two towers, genre=adventure, year=2007, price=39.0, quantity=5)', 'Book(isbn=9780261102378, title=Lord of the rings - The return of the king, genre=adventure, year=2007, price=39.0, quantity=2)']")

        self.assertRaises(IndexError, BookRepository, [
            Book("9780552779777", "The girl on the train", "adventure", 2016, 61.0, 1),
            Book("9780552779777", "The girl on the train", "adventure", 2016, 61.0, 1)  
        ])

    def test_len(self):
        self.assertEqual(len(self.empty_repository), 0)
        self.assertEqual(len(self.book_repository), 1)
        self.assertEqual(len(self.lor_repository), 3)
