from Domain.entities import Person
from Domain.entities import Event
from datetime import datetime


class Console:
    def __init__(self, events_service, people_service, events_file, people_file):
        self.__events_service = events_service
        self.__people_service = people_service
        self.__events_file = events_file
        self.__people_file = people_file

    def console_start(self):
        print("Welcome the Event Organizer. For a list of commands type \"help\".")
        self.__console()

    def __console(self):
        command = self.__read_command()
        # Add
        if command[0] == "add":
            if len(command) < 2:
                self.__invalid_command()
            else:
                # Person
                if command[1] == "person":
                    person = self.__read_person()
                    if person is not None:
                        op = self.__people_service.add_person(person)
                        if not op:
                            self.__id_exception()
                        else:
                            self.__positive_feedback()
                # Event
                elif command[1] == "event":
                    event = self.__read_event()
                    if event is not None:
                        op = self.__events_service.add_event(event)
                        if not op:
                            self.__id_exception()
                        else:
                            self.__positive_feedback()
                # Invalid
                else:
                    self.__invalid_command()
        # Delete
        elif command[0] == "delete":
            if len(command) < 2:
                self.__invalid_command()
            else:
                # Persoana
                if command[1] == "person":
                    op = self.__people_service.delete_person(command[2])
                    if not op:
                        self.__id_not_found()
                    else:
                        self.__events_service.unregister_participant(command[2])
                        self.__positive_feedback()
                # Event
                elif command[1] == "event":
                    participants = self.__events_service.get_event_participants(command[2])
                    op = self.__events_service.delete_event(command[2])
                    if not op:
                        self.__id_not_found()
                    else:
                        self.__people_service.decrement_events(participants)
                        self.__positive_feedback()
                # Invalid
                else:
                    self.__invalid_command()
        # Modify
        elif command[0] == "modify":
            if len(command) < 2:
                self.__invalid_command()
            else:
                # Person
                if command[1] == "person":
                    person = self.__read_person()
                    op = self.__people_service.modify_person(person)
                    if not op:
                        self.__id_not_found()
                    else:
                        self.__positive_feedback()
                # Event
                elif command[1] == "event":
                    op = self.__events_service.modify_event(command[2])
                    if not op:
                        self.__id_not_found()
                    else:
                        self.__positive_feedback()
                # Invalid
                else:
                    self.__invalid_command()
        # List
        elif command[0] == "list":
            if len(command) < 2:
                self.__invalid_command()
            else:
                # People
                if command[1] == "people":
                    print(self.__people_service.list_people())
                # Evenets
                elif command[1] == "events":
                    print(self.__events_service.list_events())
                # Invalid
                else:
                    self.__invalid_command()
        # Search
        elif command[0] == "search":
            if len(command) < 3:
                self.__invalid_command()
            else:
                search_string = command[2]
                for i in range(3, len(command)):
                    search_string += " " + command[i]
                # People
                if command[1] == "people":
                    print(self.__people_service.search_people(search_string))
                # Events
                elif command[1] == "events":
                    print(self.__events_service.search_events(search_string))
                # Invalid
                else:
                    self.__invalid_command()
        # Generate
        elif command[0] == "generate":
            self.__people_service.generate_people()
            self.__positive_feedback()
        # Register person
        elif command[0] == "register":
            if len(command) < 3:
                self.__invalid_command()
            else:
                person = self.__people_service.get_participant(command[1])
                if person is None:
                    op = self.__events_service.register_participant(command[1], command[2])
                    if not op:
                        self.__event_id_error()
                    elif op is None:
                        self.__already_registered()
                    else:
                        self.__people_service.increment_events(command[1])
                        self.__positive_feedback()
                else:
                    self.__person_id_error()
        # Report
        elif command[0] == "report":
            # People
            if command[1] == "people":
                print(self.__people_service.report_most_active_people())
            # Events - sorted by description
            elif len(command) == 3 and command[1] == "events":
                print(self.__events_service.report_events(command[2], False))
            # Events - sorted by date
            elif len(command) == 4 and command[1] == "events" and command[3] == "date":
                print(self.__events_service.report_events(command[2], True))
            # 20%
            elif command[1] == "20%":
                print(self.__events_service.report_20_percent())
            # Invalid
            else:
                self.__invalid_command()
        # Help
        elif command[0] == "help":
            self.__print_help()
        # Save data
        elif command[0] == "save":
            # Events
            events = self.__events_service.get_events()
            op = self.__events_file.save_to_file(events)
            if op:
                self.__save_events_positive_feedback()
            else:
                self.__ioerror_write_events()
            # People
            people = self.__people_service.get_people()
            op = self.__people_file.save_to_file(people)
            if op:
                self.__save_people_positive_feedback()
            else:
                self.__ioerror_write_people()

        # Load data
        elif command[0] == "load":
            # Events
            events_from_file = self.__events_file.load_from_file()
            if events_from_file is None:
                self.__ioerror_read_events()
            else:
                self.__events_service.replace_events(events_from_file)
                self.__load_events_positive_feedback()
            # People
            people_from_file = self.__people_file.load_from_file()
            if people_from_file is None:
                self.__ioerror_read_people()
            else:
                self.__people_service.replace_people(people_from_file)
                self.__load_people_positive_feedback()
        # Exit
        elif command[0] == "exit":
            return
        # Invalid command
        else:
            self.__invalid_command()
        self.__console()

    def __read_command(self):
        command = input("Your command: ").split()
        if len(command) == 0:
            return self.__read_command()
        return command

    def __read_person(self):
        person_id = input("ID = ")
        try:
            int(person_id)
        except ValueError:
            self.__id_not_number()
            return None
        name = input("Name = ")
        address = input("Address = ")
        person = Person(int(person_id), name, address)
        return person

    def __read_event(self):
        event_id = input("ID = ")
        try:
            int(event_id)
        except TypeError:
            self.__id_not_number()
            return None
        date = input("Date (year/month/day) = ")
        try:
            datetime.strptime(date, "%Y/%m/%d")
        except TypeError:
            self.__invalid_format()
            return None
        time = input("Time (24 hours format) = ")
        try:
            datetime.strptime(time, "%H:%M")
        except TypeError:
            self.__invalid_format()
            return None
        description = input("Description = ")
        event = Event(event_id, date, time, description)
        return event

    @staticmethod
    def __print_help():
        print("help - prints this menu")
        print("add person - adds a new person")
        print("add event - adds a new event")
        print("delete person <ID> - deletes the person who's ID is <ID>")
        print("delete event <ID> - deletes the event with the ID equal to <ID>")
        print("modify person <ID> - modifies the person who's ID <ID>")
        print("modify event <ID> - modifies the event with the ID equal to <ID>")
        print("list people - prints the list of people")
        print("list events - prints the list of events")
        print("search people <name> - prints the people with names that contain <name>")
        print("search events <description> - prints the events with descriptions that contain <description>")
        print("generate - generates a random number of people (Polish?)")
        print("register <person_ID> <event_ID> - registers a person to an event")
        print("report events <person_ID> - prints the events at which the person with the id <personID> takes part, "
              "sorted alphabetically by description")
        print("report events <person_ID> date - prints the events at which the person with the id <personID> "
              "takes part, sorted by date")
        print("report people - prints the top 5 people that take part in most events")
        print("report 20% - prints the top 20% events by participants (description, participants count)")
        print("save - saves all the data (people and events, overwrites the previously saved data)")
        print("load - loads all the data (people and events) previously saved (replaces the current data)")
        print("exit - closes the app")

    @staticmethod
    def __invalid_command():
        print("Invalid command. For a list of commands type \"help\".")

    @staticmethod
    def __id_exception():
        print("Invalid ID. Type an unique ID.")

    @staticmethod
    def __id_not_found():
        print("The ID entered doesn't exist.")

    @staticmethod
    def __id_not_number():
        print("The ID must be a number.")

    @staticmethod
    def __invalid_format():
        print("Invalid format.")

    @staticmethod
    def __positive_feedback():
        print("Operation performed succsessfully.")

    @staticmethod
    def __person_id_error():
        print("A person with the given ID doesn't exist.")

    @staticmethod
    def __event_id_error():
        print("An event with the given ID doesn't exist.")

    @staticmethod
    def __already_registered():
        print("That person is already registered to that event.")

    @staticmethod
    def __ioerror_read_events():
        print("Error reading from file \"events.txt\"")

    @staticmethod
    def __ioerror_read_people():
        print("Error reading from file \"people.txt\"")

    @staticmethod
    def __ioerror_write_events():
        print("Error writing to file \"events.txt\"")

    @staticmethod
    def __ioerror_write_people():
        print("Error writing to file \"people.txt\"")

    @staticmethod
    def __load_events_positive_feedback():
        print("Reading from file \"events.txt\" was successful.")

    @staticmethod
    def __load_people_positive_feedback():
        print("Reading from file \"people.txt\" was successful.")

    @staticmethod
    def __save_events_positive_feedback():
        print("Writing to file \"events.txt\" was successful.")

    @staticmethod
    def __save_people_positive_feedback():
        print("Writing to file \"people.txt\" was successful.")
