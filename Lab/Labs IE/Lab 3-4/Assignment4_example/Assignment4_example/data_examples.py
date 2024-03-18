from application.controller import BookController
from infrastructure.book_repository import BookRepository
from domain.book_model import Book

if __name__ == "__main__":
    controller = BookController(BookRepository([
        Book("9780261102354", "Lord of the rings - The fellowship of the ring", "adventure", 1991, 40.0, 0),
        Book("9780261102361", "Lord of the rings - The two towers", "adventure", 2007, 39.0, 5),
        Book("9780261102378", "Lord of the rings - The return of the king", "adventure", 2007, 39.0, 2)
    ]))
    hobbit = Book("9780261102217", "The hobbit", "romance", 2006, 44.0, 9)
    print("ORIGINAL LIST:", controller)
    print("-" * 100)

    controller.add_book(hobbit)
    print("AFTER ADDING An EXISTING BOOK:", controller)
    print("-" * 100)

    controller.add_new_book("9781489444943", "Schindler's list", "bibliography", 1994, 121.99, 1)
    print("AFTER ADDING A NEW BOOK:", controller)
    print("-" * 100)

    print("BOOK AT INDEX 2:", controller.get_index(2))
    print("-" * 100)

    print("BOOK WITH ISBN '9780261102217':", controller.get_isbn("9780261102217"))
    print("-" * 100)

    print("BOOKS WITH 'ADVENTURE' genre:", controller.get_books_with_genre("adventure"))
    print("-" * 100)

    print("AVAILABLE BOOKS:", controller.get_available_books())
    print("-" * 100)

    controller.update_index(4, "SCHINDLER'S LIST", "bibliography", 1994, 50.0, 10)
    print("AFTER UPDATE 4TH INDEX:", controller.get_index(4))
    print("-" * 100)

    controller.update_isbn("9781489444943", "Schindler's list", "bibliography", 1994, 50.0, 10)
    print("AFTER UPDATE BOOK WITH ISBN '9781489444943':", controller.get_isbn("9781489444943"))
    print("-" * 100)

    controller.update_books_with_genre("adventure", 0)
    print("UPDATE QUANTITY OF 'ADVENTURE' BOOKS:", controller.get_books_with_genre("adventure"))
    print("-" * 100)

    print("CURRENT STATE OF THE LIST:", controller)
    controller.delete_index(0)
    print("AFTER DELETING ELEMENT AT INDEX 0:", controller)
    print("-" * 100)

    controller.delete_isbn("9780261102361")
    print("AFTER DELETING BOOK WITH ISBN '9780261102361':", controller)
    print("-" * 100)

    controller.delete_not_available_books()
    print("AFTER DELETING NOT AVAILABLE BOOKS:", controller)
