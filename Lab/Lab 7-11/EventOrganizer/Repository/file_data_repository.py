from Domain.entities import Event
from Domain.entities import Person


class EventsFileRepo:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Loads events from file and returns them as a dictionary
        :return: events
        :rtype: {ID_event : Event}
        """
        events = {}
        try:
            file = open(self.__filename, "r")
        except IOError:
            return None
        lines = file.readlines()
        for row in lines:
            event_id, date, time, description = [token.strip() for token in row.split(";")]
            event = Event(event_id, date, time, description)
            events[event.get_id()] = event
        file.close()
        return events

    def save_to_file(self, events):
        """
        Saves events to the file or returns False if there are errors writing to file
        :param events: saved events
        :type events: {ID_event : Event}
        :return: True if the operation was succesful, otherwise False
        :rtype: bool
        """
        try:
            file = open(self.__filename, "w")
        except IOError:
            return False
        for ID in events:
            event_string = str(ID) + ";" + events[ID].get_date() + ";" + events[ID].get_time() + ";" + \
                           events[ID].get_description() + '\n'
            file.write(event_string)
        file.close()
        return True
            

class PeopleFileRepo:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Loads people from file and returns them as a dictionary
        :return: people
        :rtype: {ID_person : Person}
        """
        people = {}
        try:
            file = open(self.__filename, "r")
        except IOError:
            return None
        lines = file.readlines()
        for row in lines:
            person_id, name, address = [token.strip() for token in row.split(";")]
            person = Person(person_id, name, address)
            people[person.get_id()] = person
        file.close()
        return people

    def save_to_file(self, people):
        """
        Saves people to the file or returns False if there are errors writing to file
        :param people: people to save
        :type people: {ID_event : Person}
        :return: True if the operation was succesful, otherwise False
        :rtype: bool
        """
        try:
            file = open(self.__filename, "w")
        except IOError:
            return False
        for ID in people:
            person_string = str(ID) + ";" + people[ID].get_name() + ";" + people[ID].get_address() + '\n'
            file.write(person_string)
        file.close()
        return True
