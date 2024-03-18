class Book:
    '''
    Represents a book which has the following attributes:
        - isbn     - unique identifier of a book
        - title
        - genre    - has to be one of the values defined in the list below
        - year     - publication year (has to be between 1450 and 2020 - the current year)
        - price    - price of the book (it has to be greater than 0)
        - quantity - number of copies available (it has to be positive or zero)
    The class could raise several error in it's methods which will be explained in the documentation of the functions
    '''

    genres = [ "classic", "action", "historical fiction", "adventure", "romance", "sci-fi", "bibliography" ]

    def __init__(self, isbn: str, title: str, genre: str, publication_year: int, price: float, quantity: int = 0):
        '''
        Constructor of the class. Creates a new Book instance
        
        Args:
        -----
            @isbn: str
                unique identifier of the book
            @title: str
                title of the book
            @genre: str
                genre of the book
            @publication_year: int
                publication year of the book
            @price: float
                price of the book
        
        Keyword args:
        -------------
            @quantity: int, optional
                number of copies available. Defaults to 0.
        
        Raises:
        -------
            AttributeError
                raised if `genre` is not one of the given values
            AttributeError
                raised if `publication_year` is lower than 1450
            AttributeError
                raised if `publication_year` is greater than the current year 2020
            AttributeError
                raised if the `price` is negative or zero
            AttributeError
                raised if the `quantity` is negative
        '''
        self.__isbn = isbn
        self.__title = title

        if genre not in Book.genres:
            raise AttributeError(f"'{genre}' is not a known genre.\n Genre has to be one from {Book.genres}")
        self.__genre = genre

        if publication_year < 1450:
            raise AttributeError("The first book was printed in the 1450s")
        elif publication_year > 2020:
            raise AttributeError(f"{publication_year} is in the furute")
        self.__year = publication_year

        if price <= 0:
            raise AttributeError("Price has to be positive!")
        self.__price = price

        if quantity < 0:
            raise AttributeError("Quantity has to be positive!")
        self.__quantity = quantity

        
    #########################################
    #   GETTERS AND SETTERS                 #
    #########################################

    def get_isbn(self) -> str:
        '''
        Returns:
        --------
            str
                ISBN of the current book
        '''
        return self.__isbn

    def set_isbn(self, new_isbn: str):
        '''
        Set new value to ISBN
        
        Args:
        -----
            @new_isbn: str
                unique identifier of the book
        '''
        self.__isbn = new_isbn

    def get_title(self) -> str:
        '''
        Returns:
        --------
            str
                title of the current book
        '''
        return self.__title

    def set_title(self, new_title: str):
        '''
        Set new value to title
        
        Args:
        -----
            @new_title: str
                title of the book
        '''
        self.__title = new_title

    def get_genre(self) -> str:
        '''     
        Returns:
        --------
            str
                genre of the current book
        '''
        return self.__genre

    def set_genre(self, new_genre: str):
        '''
        Set new value to genre
        
        Args:
        -----
            @new_genre: str
                genre of the book
        
        Raises:
        -------
            AttributeError
                raised if `new_genre` is not one of the given values
        '''
        if new_genre not in Book.genres:
            raise AttributeError(f"'{new_genre}' is not a known genre.\n Genre has to be one from {Book.genres}")
        self.__genre = new_genre

    def get_year(self) -> int:
        '''                
        Returns:
        --------
            int
                publication year of the book
        '''
        return self.__year

    def set_year(self, new_year: int):
        '''
        Set new value to publication year
        
        Args:
        -----
            @new_year: int
                publication year of the book
        
        Raises:
        -------
            AttributeError
                raised if `new_year` is lower than 1450
            AttributeError
                raised if `new_year` is greater than the current year 2020
        '''
        if new_year < 1450:
            raise AttributeError("The first book was printed in the 1450s")
        elif new_year > 2020:
            raise AttributeError(f"{new_year} is in the furute")
        self.__year = new_year

    def get_price(self) -> float:
        '''  
        Returns:
        --------
            float
                price of the current book
        '''
        return self.__price

    def set_price(self, new_price: float):
        '''
        Set new value to the book's price
        
        Args:
        -----
            @new_price: float
                price of the book
        
        Raises:
        -------
            AttributeError
                raised if the `new_price` is negative or zero
        '''
        if new_price <= 0:
            raise AttributeError("Price has to be positive!")
        self.__price = new_price

    def get_quantity(self) -> int:
        '''
               
        Returns:
        --------
            int
                quantity, number of copies available from the current book
        '''
        return self.__quantity

    def set_quantity(self, new_quantity: int):
        '''
        Set new value to quantity
        
        Args:
        -----
            @new_quantity: int
                number of copies available
        
        Raises:
        -------
            AttributeError
                raised if the `new_quantity` is negative
        '''
        if new_quantity < 0:
            raise AttributeError("Quantity has to be positive!")
        self.__quantity = new_quantity

    def __str__(self) -> str:
        '''
        Returns:
        --------
            str
                string representation of the current book instance
        '''
        return f"Book(isbn={self.__isbn}, title={self.__title}, genre={self.__genre}, year={self.__year}, price={self.__price}, quantity={self.__quantity})"

    def __eq__(self, other) -> bool:
        '''
        Defines if two Book instances are equal or not
        
        Args:
        -----
            @other: Book
                another Book instance to compare to the current
        
        Returns:
        --------
            bool
                True if the two objects attribute are the same, False otherwise
        '''
        return self.__isbn == other.__isbn and \
            self.__title == other.__title and \
            self.__genre == other.__genre and \
            self.__year == other.__year and \
            self.__price == other.__price and \
            self.__quantity == other.__quantity

    #########################################
    #   FEATURES                            #
    #########################################

    def title_contains(self, word: str) -> bool:
        '''
        Defines if the title contains a specific word (the case don't have to match).
        
        Args:
        -----
            @word: str
                the word we are looking for in the title
        
        Returns:
        --------
            bool
                True if the word can be found in the title, False otherwise
        '''
        return word.lower() in self.__title.lower()

    def publicated_between_years(self, year1: int, year2: int) -> bool:
        '''
        Defines if the current book was published between two given years.
        
        Args:
        -----
            @year1: int
                start year
            @year2: int
                end year
        
        Returns:
        --------
            bool
                True if the current book was published between year1 and year2, False otherwise
        '''
        return year1 <= self.__year <= year2

    def is_at_stock(self) -> bool:
        '''
        Defines if the current book is available 
        
        Returns:
        --------
            bool
                True if there are more than 0 copy from the current book, False otherwise
        '''
        return self.__quantity > 0
