from Repository.repo import *
from Domain.entities import *
import unittest

class TestAddRemoveUpdateBook(unittest.TestCase):
    def setUp(self):
        """
            This function is called before any test cases.
            We can add initialization code common to all methods here
                (e.g. reading an input file)
        """
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def test_add_book(self):
        repo = Repo('book')
        self.assertEqual(len(repo.getAll()),0)
        b1 = Book(12, "Book1", "Auth1")
        b2 = Book(13, "Book2", "Auth2")
        b3 = Book(14, "Book3", "Auth3")
        b4 = Book(15, "Book4", "Auth4")
        repo.add(b1)
        self.assertEqual(repo.getAll(),[b1],"This is where the error occurs!")
        repo.add(b2)
        self.assertEqual(repo.getAll(),[b1,b2])
        repo.add(b3)
        repo.add(b4)
        self.assertEqual(repo.getAll(),[b1,b2,b3,b4])
        with self.assertRaises(RepoError):
            repo.add(b1)
        with self.assertRaises(RepoError):
            repo.add(b4)

    def test_remove_book(self):
        repo = Repo('book')
        b1 = Book(12, "Book1", "Auth1")
        b2 = Book(13, "Book2", "Auth2")
        b3 = Book(14, "Book3", "Auth3")
        repo.add(b1)
        repo.add(b2)
        repo.add(b3)
        repo.remove(b1)
        self.assertEqual(repo.getAll(),[b2, b3])
        repo.remove(b2)
        self.assertEqual(repo.getAll(),[b3])
        repo.remove(b3)
        self.assertEqual(repo.getAll(),[])
        b4 = Book(15, "Book4", "Auth4")
        with self.assertRaises(RepoError):
            repo.remove(b4)

    def test_update_book(self):
        repo = Repo('book')
        b1 = Book(12, "Book1", "Auth1")
        repo.add(b1)
        newBook = Book(13, "Book2", "Auth2")
        repo.update(b1, newBook)
        self.assertEqual(repo.getAll(),[newBook])
        with self.assertRaises(RepoError):
            repo.update(b1, newBook)

    def test_add_client(self):
        repo = Repo('client')
        self.assertEqual(len(repo.getAll()),0)
        c1 = Client(12, "c1")
        c2 = Client(13, "c2")
        c3 = Client(14, "c3")
        c4 = Client(15, "c4")
        repo.add(c1)
        self.assertEqual(repo.getAll(),[c1],"This is where the error occurs!")
        repo.add(c2)
        self.assertEqual(repo.getAll(),[c1,c2])
        repo.add(c3)
        repo.add(c4)
        self.assertEqual(repo.getAll(),[c1,c2,c3,c4])
        with self.assertRaises(RepoError):
            repo.add(c1)
        with self.assertRaises(RepoError):
            repo.add(c4)

    def test_remove_client(self):
        repo = Repo('client')
        c1 = Client(12, "c1")
        c2 = Client(13, "c2")
        c3 = Client(14, "c3")
        repo.add(c1)
        repo.add(c2)
        repo.add(c3)
        repo.remove(c1)
        self.assertEqual(repo.getAll(),[c2, c3])
        repo.remove(c2)
        self.assertEqual(repo.getAll(),[c3])
        repo.remove(c3)
        self.assertEqual(repo.getAll(),[])
        c4 = Client(15, "c4")
        with self.assertRaises(RepoError):
            repo.remove(c4)

    def test_update_client(self):
        repo = Repo('client')
        c1 = Client(12, "c1")
        repo.add(c1)
        newClient = Client(13, "c2")
        repo.update(c1, newClient)
        self.assertEqual(repo.getAll(),[newClient])
        with self.assertRaises(RepoError):
            repo.update(c1, newClient)

'''
def test_add_book():
    repo = RepoBooks()
    b1 = Book(12,"Book1","Auth1")
    b2 = Book(13,"Book2","Auth2")
    b3 = Book(14,"Book3","Auth3")
    b4 = Book(15,"Book4","Auth4")
    repo.addBook(b1)
    assert repo.getBooks() == [b1]
    repo.addBook(b2)
    assert repo.getBooks() == [b1,b2]
    repo.addBook(b3)
    repo.addBook(b4)
    assert repo.getBooks() == [b1,b2,b3,b4]
    try:
        repo.addBook(b1)
        repo.addBook(b2)
        repo.addBook(b4)
        assert False
    except RepoError:
        assert True

def test_remove_book():
    repo = RepoBooks()
    b1 = Book(12, "Book1", "Auth1")
    b2 = Book(13, "Book2", "Auth2")
    b3 = Book(14, "Book3", "Auth3")
    repo.addBook(b1)
    repo.addBook(b2)
    repo.addBook(b3)
    repo.removeBook(b1)
    assert repo.getBooks() == [b2,b3]
    repo.removeBook(b2)
    assert repo.getBooks() == [b3]
    repo.removeBook(b3)
    assert repo.getBooks() == []
    b4 = Book(15, "Book4", "Auth4")
    try:
        repo.removeBook(b4)
        assert False
    except RepoError:
        assert True

def test_update_book():
    repo = RepoBooks()
    b1 = Book(12, "Book1", "Auth1")
    repo.addBook(b1)
    newBook = Book(13, "Book2", "Auth2")
    repo.updateBook(b1,newBook)
    assert repo.getBooks() == [newBook]
    try:
        repo.updateBook(b1,newBook)
        assert False
    except RepoError:
        assert True


def run_all_tests():
    test_add_book()
    test_remove_book()
    test_update_book()
'''
