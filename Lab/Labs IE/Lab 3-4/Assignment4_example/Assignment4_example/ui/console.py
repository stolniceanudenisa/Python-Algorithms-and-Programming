from application.controller import BookController
from domain.book_model import Book

def print_menu():
    print("\nType '1' to list all commands\nType '0' to finish the program")
    print("0 - exit")
    print("1 - help")
    print("2 - list content of the repository")
    print("3 - add new book")
    print("4 - get book at index")
    print("5 - get book with ISBN")
    print("6 - get books with genre")
    print("7 - get available books")
    print("8 - update book at index")
    print("9 - update book with ISBN")
    print("10 - update book quantity with genre")
    print("11 - delete book at index")
    print("12 - delete book with isbn")
    print("13 - delete not available books")

def run(controller: BookController):
    print_menu()
    command = input(">>> ")
    while command != "0":
        if command == "1":
            print_menu()

        elif command == "2":
            print(controller)

        elif command == "3":
            print("\nAdd new book to the list")
            isbn = input("ISBN = ")
            title = input("Title = ")
            genre = input("Genre = ")
            try:
                year = int(input("Publication year = "))
                price = float(input("Price = "))
                quantity = int(input("Quantity = "))

                controller.add_new_book(isbn, title, genre, year, price, quantity)
            except ValueError as ex:
                print(f"Enter int/float numbers.\n{ex}")
            except (IndexError, AttributeError) as ex:
                print(ex)

        elif command == "4":
            print("\nGet book at index")
            try:
                index = int(input("Index = "))

                print(controller.get_index(index))
            except ValueError as ex:
                print(f"You have to enter an integer value\n{ex}")
            except IndexError as ex:
                print(ex)
                
        elif command == "5":
            print("\nGet book with ISBN")
            isbn = input("ISBN = ")
            try:
                print(controller.get_isbn(isbn))
            except IndexError as ex:
                print(ex)

        elif command == "6":
            print("\nBooks with a given genre")
            genre = input("Genre = ")
            print(controller.get_books_with_genre(genre))

        elif command == "7":
            print("\nBooks that are available")
            print(controller.get_available_books()) 

        elif command == "8":
            print("\nUpdate book at index")
            try:
                index = int(input("Index = "))
                title = input("Title = ")
                genre = input("Genre = ")
                year = int(input("Publication year = "))
                price = float(input("Price = "))
                quantity = int(input("Quantity = "))

                controller.update_index(index, title, genre, year, price, quantity)
            except ValueError as ex:
                print(f"Enter int/float numbers.\n{ex}")
            except (IndexError, AttributeError) as ex:
                print(ex)

        elif command == "9":
            print("\nUpdate book with ISBN")
            isbn = input("ISBN = ")
            title = input("Title = ")
            genre = input("Genre = ")
            try:
                year = int(input("Publication year = "))
                price = float(input("Price = "))
                quantity = int(input("Quantity = "))

                controller.update_isbn(isbn, title, genre, year, price, quantity)
            except ValueError as ex:
                print(f"Enter int/float numbers.\n{ex}")
            except (IndexError, AttributeError) as ex:
                print(ex)

        elif command == "10":
            print("\nUpdate book quantity with genre")
            genre = input("Genre = ")
            try:
                quantity = int(input("Quantity = "))

                controller.update_books_with_genre(genre, quantity)
            except ValueError as ex:
                print(f"You have to enter an integer value\n{ex}")
            except AttributeError as ex:
                print(ex)

        elif command == "11":
            print("\nDelete book at index")
            try:
                index = int(input("Index = "))

                controller.delete_index(index)
            except ValueError as ex:
                print(f"You have to enter an integer value\n{ex}")
            except IndexError as ex:
                print(ex)

        elif command == "12":
            print("\nDelete book with ISBN")
            isbn = input("ISBN = ")
            try:
                controller.delete_isbn(isbn)
            except IndexError as ex:
                print(ex)

        elif command == "13":
            print("\nDelete not available books")
            controller.delete_not_available_books()

        else:
            print(f"'{command}' not defined")

        # in case we modifies something in the list we print the current content
        if command in [ "3", "8", "9", "10", "11", "12", "13" ]:
            print(f"Content of the repository: {controller}")

        command = input(">>> ")

    print("Bye bye\n")