# Library-App
Application for a book library. Object oriented programming implemented.

--------------------------------------------------------------------

The application will store:

 Book: bookId, title, author.
  
 Client: clientId, name.
  
 Rental: rentalID, bookId, clientId, rented date, returned date.
  
The application allows the user to:
  
1. Manage the list of clients and books. The application must allow the user to add, remove, update,
and list both clients and books.
  
2. Rent or return a book. A client can rent an available book. A client can return a rented book at any
time. Only available books can be rented.
  
3. Search for clients or books using any one of their fields (e.g. books can be searched for using id, title
or author). The search must work using case-insensitive, partial string matching, and must return all
matching items.
  
4. Create statistics:

 Most rented books. This will provide the list of books, sorted in descending order of the number
of times they were rented.

 Most active clients. This will provide the list of clients, sorted in descending order of the number
of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6
days).

 Most rented author. This provides the list of book authored, sorted in descending order of the
number of rentals their books have.

5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by
the user. Undo/redo operations must cascade and have a memory-efficient implementation (no
superfluous list copying).
