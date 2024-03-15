from Domain.entities import SearchError,UIError
import datetime
import PySimpleGUI

class GUI:
    def __init__(self,BookSrv,ClientSrv,RentalSrv,StatisticsSrv,UndoRedoSrv):
        self.__BookSrv = BookSrv
        self.__ClientSrv = ClientSrv
        self.__RentalSrv = RentalSrv
        self.__StatSrv = StatisticsSrv
        self.__UndoRedoSrv = UndoRedoSrv
        self.__GUI = PySimpleGUI
        self.__GUI.change_look_and_feel('Dark')

    @staticmethod
    def list_of_objects(objList):
        return "\n".join([str(objList.index(obj)+1)+'. '+str(obj) for obj in objList])

    # The callback functions
    def button1(self):
       clientList = self.__ClientSrv.srv_getClientList()
       theClients = self.list_of_objects(clientList)
       if not len(clientList):
           raise Exception("There are no clients!\n")
       self.__GUI.PopupScrolled(theClients, title='The clients', size=(40, 22), non_blocking=True,location=(20,10))

    def button2(self):
        bookList = self.__BookSrv.srv_getBookList()
        theBooks = self.list_of_objects(bookList)
        if not len(bookList):
            raise Exception("There are no books!\n")
        self.__GUI.PopupScrolled(theBooks, title="The books", size=(100, 40), non_blocking=True,location=(725,10))

    def button3(self):
       form = self.__GUI.FlexForm('Add book')  # begin with a blank form
       Layout = [
          [self.__GUI.Text('Please enter the ID, title and author of the book:')],
          [self.__GUI.Text('ID', size=(15, 1)),self.__GUI.InputText()],
          [self.__GUI.Text('Title', size=(15, 1)),self.__GUI.InputText()],
          [self.__GUI.Text('Author', size=(15, 1)),self.__GUI.InputText()],
          [self.__GUI.Submit(), self.__GUI.Cancel()]]
       button, values = form.Layout(Layout).Read()
       if str(button) == 'Cancel':
          form.close()
          return
       form.close()
       self.__BookSrv.add_book(int(values[0]),values[1].strip(), values[2].strip())
       self.__GUI.Popup("Book added successfully!",title='Done',auto_close=True)

    def button4(self):
        form = self.__GUI.FlexForm('Remove book')
        Layout = [
            [self.__GUI.Text('Please enter the ID of the book that you want to remove:')],
            [self.__GUI.Text('ID', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Submit(), self.__GUI.Cancel()]]
        button, value = form.Layout(Layout).Read()
        if str(button) == 'Cancel':
            form.close()
            return
        form.close()
        self.__RentalSrv.remove_book_and_rentals(int(value[0]))
        self.__GUI.Popup("Book removed successfully!",title='Done',auto_close=True)

    def button5(self):
        form = self.__GUI.FlexForm('Update book')
        Layout = [
            [self.__GUI.Text('Please enter the ID, the NEW title and the NEW author for the book:')],
            [self.__GUI.Text('ID', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Text('New title', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Text('New author', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Submit(), self.__GUI.Cancel()]]
        button, values = form.Layout(Layout).Read()
        if str(button) == 'Cancel':
            form.close()
            return
        form.close()
        self.__BookSrv.update_book(int(values[0]), values[1].strip(), values[2].strip())
        self.__GUI.Popup("Book updated successfully!",title='Done',auto_close=True)

    def button6(self):
       form = self.__GUI.FlexForm('Add client')
       Layout = [
          [self.__GUI.Text('Please enter the ID and the name of the client:')],
          [self.__GUI.Text('ID', size=(15, 1)),self.__GUI.InputText()],
          [self.__GUI.Text('Name', size=(15, 1)),self.__GUI.InputText()],
          [self.__GUI.Submit(), self.__GUI.Cancel()]]
       button, values = form.Layout(Layout).Read()
       if str(button) == 'Cancel':
          form.close()
          return
       form.close()
       self.__ClientSrv.add_client(int(values[0]),values[1].strip())
       self.__GUI.Popup("Client added successfully!",title='Done',auto_close=True)

    def button7(self):
        form = self.__GUI.FlexForm('Remove client')
        Layout = [
            [self.__GUI.Text('Please enter the ID of the client that you want to remove:')],
            [self.__GUI.Text('ID', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Submit(), self.__GUI.Cancel()]]
        button, value = form.Layout(Layout).Read()
        if str(button) == 'Cancel':
            form.close()
            return
        form.close()
        self.__RentalSrv.remove_client_and_rentals(int(value[0]))
        self.__GUI.Popup("Client removed successfully!",title='Done',auto_close=True)

    def button8(self):
        form = self.__GUI.FlexForm('Update client')
        Layout = [
            [self.__GUI.Text('Please enter the ID and the NEW name for the client:')],
            [self.__GUI.Text('ID', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Text('New name', size=(15, 1)), self.__GUI.InputText()],
            [self.__GUI.Submit(), self.__GUI.Cancel()]]
        button, values = form.Layout(Layout).Read()
        if str(button) == 'Cancel':
            form.close()
            return
        form.close()
        self.__ClientSrv.update_client(int(values[0].strip()), values[1].strip())
        self.__GUI.Popup("Client updated successfully!",title='Done',auto_close=True)

    def button9(self):
        form = self.__GUI.FlexForm('Rent book')
        Layout = [
            [self.__GUI.Text('Please enter the ID of the book to rent and the client ID:')],
            [self.__GUI.Text('Book ID', size=(8, 1)), self.__GUI.InputText(size=(30,1))],
            [self.__GUI.Text('Client ID', size=(8, 1)), self.__GUI.InputText(size=(30,1))],
            [self.__GUI.Text('Please enter the date of rent:')],
            [self.__GUI.Text("Day"),self.__GUI.InputText(size=(6,1)),self.__GUI.Text("Month"),self.__GUI.InputText(size=(6,1)),self.__GUI.Text("Year"),self.__GUI.InputText(size=(6,1))],
            [self.__GUI.Submit(), self.__GUI.Cancel()]]
        button, values = form.Layout(Layout).Read()
        if str(button) == 'Cancel':
            form.close()
            return
        form.close()
        month, day, year = int(values[3]), int(values[2]), int(values[4])
        rentDate = datetime.date(year, month, day)
        title,author = self.__BookSrv.getBookTitleAuthor(int(values[0]))
        clientName = self.__ClientSrv.getClientName(int(values[1]))
        self.__RentalSrv.rent_book(int(values[0]),int(values[1]),rentDate)
        self.__GUI.Popup("'{}' by {} was rented by {} successfully!".format(title,author,clientName), title='Done')

    def button10(self):
        form = self.__GUI.FlexForm('Return book')
        Layout = [
            [self.__GUI.Text('Please enter the ID of the book to return:')],
            [self.__GUI.Text('Book ID', size=(8, 1)), self.__GUI.InputText(size=(30, 1))],
            [self.__GUI.Text('Please enter the date of return:')],
            [self.__GUI.Text("Day"), self.__GUI.InputText(size=(6, 1)), self.__GUI.Text("Month"),
             self.__GUI.InputText(size=(6, 1)), self.__GUI.Text("Year"), self.__GUI.InputText(size=(6, 1))],
            [self.__GUI.Submit(), self.__GUI.Cancel()]]
        button, values = form.Layout(Layout).Read()
        if str(button) == 'Cancel':
            form.close()
            return
        form.close()
        month, day, year = int(values[2]), int(values[1]), int(values[3])
        retDate = datetime.date(year, month, day)
        title, author = self.__BookSrv.getBookTitleAuthor(int(values[0]))
        self.__RentalSrv.return_book(int(values[0]), retDate)
        self.__GUI.Popup("'{}' by {} was returned successfully!".format(title, author), title='Done')

    def button11(self):
        rentalList = self.__RentalSrv.srv_getRentalList()
        theRentals = self.list_of_objects(rentalList)
        if not len(rentalList):
            raise UIError("There are no rentals!\n")
        self.__GUI.PopupScrolled(theRentals, title='The rentals', size=(100, 15), non_blocking=True, location=(20, 10))

    def button12(self):
        layout = [[self.__GUI.Frame(layout=[[self.__GUI.Radio('ID', "RADIO1", default=True,size=(6,1)),self.__GUI.Radio('Title', "RADIO1",size=(6,1)),self.__GUI.Radio('Author', "RADIO1",size=(6,1))]],
        title='Search by',title_color='white', relief=self.__GUI.RELIEF_SUNKEN, tooltip='Choose your search option')],
                  [self.__GUI.Text('Search:'),self.__GUI.InputText(size=(31,1))],
                  [self.__GUI.Submit(), self.__GUI.Cancel()]]
        window = self.__GUI.Window('Search book', layout)
        fields = ('ID', 'title', 'author')
        while True:  # The Event Loop
            event, values = window.read()
            if event in (None, 'Exit','Cancel'):
                window.close()
                break
            choice =  [i for i in range(0,3) if values[i]][0]
            split_search_input = values[3].split()
            try:
                found_books = self.__BookSrv.search_books(fields[choice], split_search_input)
                found_books_STR = self.list_of_objects(found_books)
                self.__GUI.PopupScrolled(found_books_STR, title="The found books", size=(100, 20), non_blocking=True,location=(725, 10))
            except SearchError as error:
                self.__GUI.Popup(error, title='Error')
        window.close()

    def button13(self):
        layout = [[self.__GUI.Frame(layout=[[self.__GUI.Radio('ID', "RADIO1", default=True, size=(11, 1)),self.__GUI.Radio('Name', "RADIO1", size=(11, 1))]],
                                    title='Search by', title_color='white', relief=self.__GUI.RELIEF_SUNKEN,tooltip='Choose your search option')],
                  [self.__GUI.Text('Search:'), self.__GUI.InputText(size=(30, 1))],
                  [self.__GUI.Submit(), self.__GUI.Cancel()]]
        window = self.__GUI.Window('Search client', layout)
        fields = ('ID', 'name')
        while True:  # The Event Loop
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                window.close()
                break
            choice = [i for i in range(0, 2) if values[i]][0]
            split_search_input = values[2].split()
            try:
                found_clients = self.__ClientSrv.search_clients(fields[choice], split_search_input)
                found_clients_STR = self.list_of_objects(found_clients)
                self.__GUI.PopupScrolled(found_clients_STR, title="The found clients", size=(40, 22), non_blocking=True,location=(20, 10))
            except SearchError as error:
                self.__GUI.Popup(error, title='Error')
        window.close()

    def button14(self):
        sorted_bookList = self.__StatSrv.most_rented_books()
        theBooks = ''
        nr=0
        for book in sorted_bookList:
            nr+=1
            theBooks += '{}. {} - rented {} time(s)'.format(nr,book,book.getTimesRented()) + '\n'
        self.__GUI.PopupScrolled(theBooks, title="The most rented books", size=(120, 20), non_blocking=True)

    def button15(self):
        sorted_clientList = self.__StatSrv.most_active_clients()
        theClients = ''
        nr = 0
        for client in sorted_clientList:
            nr += 1
            theClients += '{}. {} - {} rental days'.format(nr, client, client.getRentalDays()) + '\n'
        self.__GUI.PopupScrolled(theClients, title="The most active clients",  size=(50, 22), non_blocking=True)

    def button16(self):
        sortedAuthors = self.__StatSrv.most_rented_authors()
        theAuthors = ''
        nr = 0
        for author in sortedAuthors:
            nr += 1
            theAuthors += "{}. {} - {} book rental(s)".format(nr, author, sortedAuthors[author]) + '\n'
        self.__GUI.PopupScrolled(theAuthors, title="The most rented authors", size=(50, 22), non_blocking=True)

    def button17(self):
        self.__UndoRedoSrv.undo()
        print("Undo complete!")
    def button18(self):
        self.__UndoRedoSrv.redo()
        print("Redo complete!")

    def run(self):
        # Layout the design of the GUI
        layout = [[self.__GUI.Text("W E L C O M E   T O   T H E   L I B R A R Y   A P P  !", auto_size_text=True,border_width=4,justification='center')],
                  [self.__GUI.Text("Choose your option:",justification='center')],
                  [self.__GUI.Button('Show Clients',size=(20,2)),self.__GUI.Button('Rent book',size=(20,2))],
                  [self.__GUI.Button('Show books',size=(20,2)),self.__GUI.Button('Return book',size=(20,2))],
                  [self.__GUI.Button('Add book',size=(20,2)),self.__GUI.Button('Show rentals',size=(20,2))],
                  [self.__GUI.Button('Remove book',size=(20,2)),self.__GUI.Button('Search book',size=(20,2))],
                  [self.__GUI.Button('Update book',size=(20,2)),self.__GUI.Button('Search client',size=(20,2))],
                  [self.__GUI.Button('Add client',size=(20,2)),self.__GUI.Button('Show most rented books',size=(20,2))],
                  [self.__GUI.Button('Remove client',size=(20,2)),self.__GUI.Button('Show most active clients',size=(20,2))],
                  [self.__GUI.Button('Update client',size=(20,2)),self.__GUI.Button('Show most rented authors',size=(20,2))],
                  [self.__GUI.Quit(size=(7,1)), self.__GUI.Text('(Pussy option) ',size=(12,1)),self.__GUI.Button('UNDO',size=(8,1)),self.__GUI.Button('REDO',size=(8,1))]]
        # Lookup dictionary that maps button to function to call
        dispatch_dictionary = {'Show Clients':self.button1,
                               'Show books':self.button2,
                               'Add book':self.button3,
                               'Remove book':self.button4,
                               'Update book':self.button5,
                               'Add client': self.button6,
                               'Remove client': self.button7,
                               'Update client': self.button8,
                               'Rent book': self.button9,
                               'Return book': self.button10,
                               'Show rentals': self.button11,
                               'Search book': self.button12,
                               'Search client': self.button13,
                               'Show most rented books': self.button14,
                               'Show most active clients': self.button15,
                               'Show most rented authors': self.button16,
                               'UNDO':self.button17,
                               'REDO':self.button18}
        # Show the Window to the user
        window = self.__GUI.Window('Library app', layout)
        # Event loop. Read buttons, make callbacks
        while True:
           try:
               # Read the Window
               event, value = window.read()
               if event in ('Quit', None):
                   break
               # Lookup event in function dictionary
               if event in dispatch_dictionary:
                   func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
                   func_to_call()
               else:
                   raise UIError("Event '{}' not in dispatch dictionary".format(event))
           except Exception as ex:
              self.__GUI.Popup(ex, title='Error')

        window.close()
        self.__GUI.Popup('Have a nice day!',title='Pussy',custom_text=('Yeah','Nah'),auto_close=True)
        exit()