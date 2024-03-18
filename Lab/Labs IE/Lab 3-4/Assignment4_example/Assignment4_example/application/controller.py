from domain.book_model import Book
from infrastructure.book_repository import BookRepository

class BookController:
    '''
    Controller class to reach the logical/domain layer.
    '''

    def __init__(self, book_repository: BookRepository = BookRepository()):
        '''
        Constructor of the class. Creating a new controller
        
        Args:
        -----
        
        Keyword args:
        -------------
            @book_repository: BookRepository, optional
                book repository which will be 'controlled' by the class. Defaults to BookRepository().
        '''
        self.__book_repository = book_repository

    def __str__(self) -> str:
        '''
        Returns:
        --------
            str
                string representation of the controller
        '''
        return str(self.__book_repository)

    def add_book(self, book: Book):
        '''
        Add existing book instance to the repository
        
        Args:
        -----
            @book: Book
        '''
        self.__book_repository.add_book(book)

    def add_new_book(self, isbn: str, title: str, genre: str, year: int, price: float, quantity: int = 0):
        '''
        Add new book instance to the repository
        
        Args:
        -----
            @isbn: str
                unique identifier of the book
            @title: str
                title of the book
            @genre: str
                genre of the book
            @year: int
                publication year of the book
            @price: float
                price of the book
        
        Keyword args:
        -------------
            @quantity: int, optional
                number of copies available. Defaults to 0.
        '''
        self.add_book(Book(isbn, title, genre, year, price, quantity))

    def get_content(self) -> list[Book]:
        '''        
        Returns:
        --------
            list[Book]
                list contained in the repository
        '''
        return self.__book_repository.get_list()

    def get_repo(self) -> BookRepository:
        '''        
        Returns:
        --------
            BookRepository
                the BookRepository instance in the current controller
        '''
        return self.__book_repository

    def get_index(self, index: int) -> Book:
        '''
        Get book at given index from the repository
        
        Args:
        -----
            @index: int
        
        Returns:
        --------
            Book
                book instance at the given index
        '''
        return self.__book_repository.get_index(index)

    def get_isbn(self, isbn: str) -> Book:
        '''
        Get book with ISBN in the repository

        
        Args:
        -----
            @isbn: str
                isbn of the book
        
        Returns:
        --------
            Book
                book instance with the given ISBN
        '''
        return self.__book_repository.get_isbn(isbn)

    def get_books_with_genre(self, genre: str) -> BookRepository:
        '''
        Get books with a given genre from the repository
        
        Args:
        -----
            @genre: str
                genre of the book
        
        Returns:
        --------
            BookRepository
                another repository containing the books which have the given genre in the current repository
        '''
        return self.__book_repository.get_books_with_genre(genre)

    def get_available_books(self) -> BookRepository:
        '''
        Get books available (quantity > 0) from the repository
        
        Returns:
        --------
            BookRepository
                another repository containing the book that are available in the current repository
        '''
        return self.__book_repository.get_available_books()

    def update_index(self, index: int, title: str, genre: str, year: int, price: float, quantity: int):
        '''
        Update book at a given index in the repository
        
        Args:
        -----
            @index: int
            @title: str
                title of the book
            @genre: str
                genre of the book
            @year: int
                publication year of the book
            @price: float
                price of the book
            @quantity: int
                number of copies available
        '''
        self.__book_repository.update_index(index, title, genre, year, price, quantity)

    def update_isbn(self, isbn: str, title: str, genre: str, year: int, price: float, quantity: int):
        '''
        Update book with ISBN in the repository
        
        Args:
        -----
            @isbn: str
                isbn of the book
            @title: str
                title of tje book
            @genre: str
                genre of the book
            @year: int
                publication year of the book
            @price: float
                price of the book
            @quantity: int
                number of copies available
        '''
        self.__book_repository.update_isbn(isbn, title, genre, year, price, quantity)

    def update_books_with_genre(self, genre: str, quantity: int):
        '''
        Update quantity of books with a given genre in the repository
        
        Args:
        -----
            @genre: str
                genre of the book
            @quantity: int
                new number of copies available
        '''
        self.__book_repository.update_books_with_genre(genre, quantity)

    def delete_index(self, index: int):
        '''
        Delete book at given index from the repository
        
        Args:
        -----
            @index: int
        '''
        self.__book_repository.delete_index(index)

    def delete_isbn(self, isbn: str):
        '''
        Delete book with ISBN in the repository
        
        Args:
        -----
            @isbn: str
                isbn of the book
        '''
        self.__book_repository.delete_isbn(isbn)
    
    def delete_not_available_books(self):
        '''
        Delete books from the repository that are not available
        '''
        self.__book_repository.delete_not_available_books()