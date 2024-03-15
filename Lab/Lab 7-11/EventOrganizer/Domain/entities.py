class Event:
    def __init__(self, event_id, date, time, description):
        self.__ID = event_id
        self.__date = date
        self.__time = time
        self.__description = description
        self.__participants = []

    def get_id(self):
        return self.__ID

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def get_participants(self):
        return self.__participants

    def set_id(self, value):
        self.__ID = value

    def set_date(self, value):
        self.__date = value

    def set_time(self, value):
        self.__time = value

    def set_description(self, value):
        self.__description = value

    def add_participant(self, event_id):
        self.__participants.append(event_id)

    def remove_participant(self, event_id):
        self.__participants.remove(event_id)


class Person:
    def __init__(self, person_id, name, address):
        self.__ID = person_id
        self.__name = name
        self.__address = address
        self.__events_count = 0

    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_events_count(self):
        return self.__events_count

    def set_id(self, value):
        self.__ID = value

    def set_name(self, value):
        self.__name = value
   
    def set_address(self, value):
        self.__address = value

    def increment_events(self):
        self.__events_count += 1

    def decrement_events(self):
        self.__events_count -= 1
