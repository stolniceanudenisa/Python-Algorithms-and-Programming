from domain.book_model import Book

class BookRepository:
    '''
    Represents a collection of Book instances
    '''

    def __init__(self, book_list: list[Book] = []):
        '''
        Constructor of the class. Creates a new collection with Book instances
        
        Args:
        -----
        
        Keyword args:
        -------------
            @book_list: list[Book], optional
                list of books in the collection. Defaults to [].
        
        Raises:
        -------
            IndexError
                raised if a book with the ISBN already exists in the repository
        '''
        self.__books = []
        for book in book_list:
            if self.__isbn_exists(book.get_isbn()):
                raise IndexError(f"The book with ISBN {book.get_isbn()} is already in the repository")
            self.__books.append(book)

    def __len__(self) -> int:
        '''
        Overwriting the len() function. With this function implemented we can use len() on any BookRepository instance and it will return the number of books in the repository.
        
        Returns:
        --------
            int
                number of books in the repository
        '''
        return len(self.__books)

    def __str__(self) -> str:
        '''
        Returns:
        --------
            str
                string representation of the current book repository instance
        '''
        books = []
        for book in self.__books:
            books.append(str(book))
        return str(books)

    def __eq__(self, other) -> bool:
        '''
        Defines if two BookRepository instances are equal or not
        
        Args:
        -----
            @other: BookRepository
                another BookRepository instance to compare to the current
        
        Returns:
        --------
            bool
                True if the two objects attribute are the same, False otherwise
        '''
        if len(self) != len(other):
            return False
        for index in range(len(self)):
            if self.__books[index] != other.__books[index]:
                return False
        return True

    def get_list(self) -> list[Book]:
        '''
        Return the list of books
        
        Returns:
        --------
            list[Book]
                list of books in the current repository
        '''
        return self.__books

    def add_book(self, book: Book):
        '''
        Add existing book instance to the repository
        
        Args:
        -----
            @book: Book
                book instance to be added to the repository
        
        Raises:
        -------
            IndexError
                raised if a book with the ISBN already exists in the repository
        '''
        if self.__isbn_exists(book.get_isbn()):
            raise IndexError(f"The book with ISBN {book.get_isbn()} is already in the repository")
        
        self.__books.append(book)
    
    def add_new_book(self, isbn: str, title: str, genre: str, year: int, price: float, quantity: int = 0):
        '''
        Ass new book to the repository
        
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
                number of books available. Defaults to 0.
        
         Raises:
        -------
            IndexError
                raised if a book with the ISBN already exists in the repository
        '''
        if self.__isbn_exists(isbn):
            raise IndexError(f"The book with ISBN {isbn} is already in the repository")

        self.__books.append(Book(isbn, title, genre, year, price, quantity))

    def get_index(self, index: int) -> Book:
        '''
        Get book at given index from the current repository
        
        Args:
        -----
            @index: int
        
        Raises:
        -------
            IndexError
                raised if the index does not exist in the repository
        
        Returns:
        --------
            Book
                book instance at the given index
        '''
        if 0 <= index < len(self):
            return self.__books[index]
        else:
            raise IndexError(f"Invalid index: {index} (0 <= index <= {len(self) - 1})")

    def get_isbn(self, isbn: str) -> Book:
        '''
        Get book with ISBN in the current repository
        
        Args:
        -----
            @isbn: str
                isbn of the book
        
        Raises:
        -------
            IndexError
                raised if the ISBN does not exist in the current repository
        
        Returns:
        --------
            Book
                book instance with the given ISBN
        '''
        if self.__isbn_exists(isbn):
            index = self.__isbn2index(isbn)
            return self.get_index(index)
        else:
            raise IndexError(f"ISBN {isbn} is not in the repository")

    def get_books_with_genre(self, genre: str):
        '''
        Get books with a given genre from the current repository
        
        Args:
        -----
            @genre: str
                genre of the book
        
        Returns:
        --------
            BookRepository
                another repository containing the books which have the given genre in the current repository
        '''
        genre_repository = BookRepository()

        for book in self.__books:
            if book.get_genre() == genre:
                genre_repository.add_book(book)
        
        return genre_repository

    def get_available_books(self):
        '''
        Get books available (quantity > 0) from the current repository
        
        Returns:
        --------
            BookRepository
                another repository containing the book that are available in the current repository
        '''
        available_repository = BookRepository()

        for book in self.__books:
            if book.is_at_stock():
                available_repository.add_book(book)

        return available_repository

    def update_index(self, index: int, title: str, genre: str, year: int, price: float, quantity: int):
        '''
        Update book at a given index in the current repository
        
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
        
        Raises:
        -------
            IndexError
                raised if the index does not exist in the repository
        '''
        if 0 <= index < len(self):
            self.__books[index].set_title(title)
            self.__books[index].set_genre(genre)
            self.__books[index].set_year(year)
            self.__books[index].set_price(price)
            self.__books[index].set_quantity(quantity)
        else:
            raise IndexError(f"Invalid index: {index} (0 <= index <= {len(self) - 1})")

    def update_isbn(self, isbn: str, title: str, genre: str, year: int, price: float, quantity: int):
        '''
        Update book with ISBN in the current repository
        
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
        
        Raises:
        -------
            IndexError
                raised if the ISBN does not exist in the current repository
        '''
        if self.__isbn_exists(isbn):
            index = self.__isbn2index(isbn)
            self.update_index(index, title, genre, year, price, quantity)
        else:
            raise IndexError(f"ISBN {isbn} is not in the repository")

    def update_books_with_genre(self, genre: str, quantity: int):
        '''
        Update quantity of books with a given genre in the current repository
        
        Args:
        -----
            @genre: str
                genre of the book
            @quantity: int
                new number of copies available
        '''
        for book in self.__books:
            if book.get_genre() == genre:
                book.set_quantity(quantity)

    def delete_index(self, index: int):
        '''
        Delete book at given index from the current repository
        
        Args:
        -----
            @index: int
        
        Raises:
        -------
            IndexError
                raised if the index does not exist in the repository
        '''
        if 0 <= index < len(self):
            del self.__books[index]
        else:
            raise IndexError(f"Invalid index: {index} (0 <= index <= {len(self) - 1})")

    def delete_isbn(self, isbn: str):
        '''
        Delete book with ISBN in the current repository
        
        Args:
        -----
            @isbn: str
                isbn of the book
        
        Raises:
        -------
            IndexError
                raised if the ISBN does not exist in the current repository
        '''
        if self.__isbn_exists(isbn):
            index = self.__isbn2index(isbn)
            self.delete_index(index)
        else:
            raise IndexError(f"ISBN {isbn} is not in the repository")

    def delete_not_available_books(self):
        '''
        Delete books from the current repository that are not available
        '''
        for index in range(len(self.__books) - 1, -1, -1):
            if not self.__books[index].is_at_stock():
                del self.__books[index]

    def __isbn_exists(self, isbn: str) -> bool:
        '''
        Check if ISBN exists in the current repository
        
        Args:
        -----
            @isbn: str
                isbn of the book
        
        Returns:
        --------
            bool
                True if a book with the ISBN already exists in the current repository, False otherwise
        '''
        for book in self.__books:
            if book.get_isbn() == isbn:
                return True
        return False

    def __isbn2index(self, isbn: str) -> int:
        '''
        Get index on which the book appears with the given ISBN in the current repository
        
        Args:
        -----
            @isbn: str
                isbn of the book
        
        Returns:
        --------
            int
                -1 if the ISBN does not exists in the corrent repository, the `index` otherwise
        '''
        for index, book in enumerate(self.__books):
            if book.get_isbn() == isbn:
                return index
        return -1
        # or
        # for index in range(len(self)):
        #     if self.__books[index].get_isbn() == isbn:
        #         return index