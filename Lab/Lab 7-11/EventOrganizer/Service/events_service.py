from Domain.entities import Event
from Repository.events_repository import EventsRepo
from Service import sorting


class EventsService:
    def __init__(self, events_repo):
        """
        Initializes service
        :param events_repo: the repository we use to store events
        :type events_repo: EventsRepo
        """
        self.__events_repo = events_repo

    def replace_events(self, events):
        """
        Replaces the events in repo with those in events
        :param events: events to replace with
        :type events: {ID_event : event}
        """
        self.__events_repo.set_events(events)

    def get_events(self):
        """
        Returns all the events from repo
        :return: events:
        :rtype: {ID_event : Event}
        """
        return self.__events_repo.get_events()

    def add_event(self, event):
        """
        Adds event
        :param event: event to add to repo
        :type event: Event
        :return: True if the event was added, False if an even with the same ID already exists
        :rtype: bool
        """
        if self.__events_repo.find(event.get_id()) is not None:
            return False
        self.__events_repo.add(event)
        return True

    def delete_event(self, event_id):
        """
        Deletes events
        :param event_id: ID of the event to delete
        :type event_id: int
        :return: True if the event was deleted, False if an event with the given ID doesn't exist
        :rtype: bool
        """
        if self.__events_repo.find(event_id) is None:
            return False
        self.__events_repo.delete(event_id)
        return True

    def modify_event(self, event):
        """
        Modifies event
        :param event: event to modify
        :type event: Event
        :return: True if the event was modified, False if an event with the same ID doesn't exist
        :rtype: bool
        """
        if self.__events_repo.find(event.get_id()) is None:
            return False
        self.__events_repo.modify(event)
        return True

    def list_events(self):
        """
        Returns the list of events or the message "The list of events is empty"
        :return: list_string - list of events from repo
        :rtype: string
        """
        list_string = ""
        events = self.__events_repo.get_events()
        for ID in events:
            list_string += str(ID) + "\t" + str(events[ID].get_date()) + "\t" + str(events[ID].get_time()) + "\t" + \
                           str(events[ID].get_description()) + "\n"
        if list_string == "":
            list_string = "The list of events is empty"
        else:
            list_string = "ID\t\tDate\t\tTime\t\tDescription\n" + list_string
        return list_string

    def search_events(self, description):
        """
        Returns the list of events which match the description or
         the message "No events with the given description were found"
        :param description: searched description
        :type description: string
        :return: list_string
        :rtype: string
        """
        list_string = ""
        events = self.__events_repo.get_events()
        for ID in events:
            if events[ID].get_description().find(description) != -1:
                list_string += str(ID) + "\t" + str(events[ID].get_date()) + "\t" + str(events[ID].get_time()) + \
                               "\t" + str(events[ID].get_description()) + "\n"
        if list_string == "":
            list_string = "No events with the given description were found"
        return list_string

    def register_participant(self, person_id, event_id):
        """
        Registers a person to an event by IDs
        :param person_id: ID of the person be registered at the event
        :type person_id: string
        :param event_id: ID of the event
        :type event_id: int
        :return: True if operation was succesful, False if event_ID is invalid, None if the person is already registered
        :rtype: bool
        """
        event = self.__events_repo.find(event_id)
        if event is None:
            return False
        if person_id in event.get_participants():
            return None
        event.add_participant(person_id)
        return True

    def unregister_participant(self, person_id):
        """
        Unregisters the person from all events
        :param person_id: ID of the person to be unregistered
        :type person_id: int
        """
        events = self.__events_repo.get_events()
        for key in events:
            if person_id in events[key].get_participants():
                events[key].remove_participant(person_id)

    def get_event_participants(self, event_id):
        """
        Returns the list with the IDs of all participants to an event
        :param event_id: ID of the event
        :type event_id: string
        :return: events[ID].getParticipants()
        :rtype: [string, string, ...]
        """
        events = self.__events_repo.get_events()
        return events[event_id].get_participants()

    def report_events(self, person_id, date):
        """
        Returns the list with the events the person with the given ID is participating in,
         ordered alphabetically by description, date or
         the message "Person with the given ID isn't participating at any events"
        :param person_id: person ID
        :type person_id: string
        :param date: True if sorting by date, False if sorting by description
        :type date: bool
        :return: list_string
        :rtype: string
        """
        list_string = ""
        events_list = []
        events = self.__events_repo.get_events()
        for ID in events:
            if person_id in events[ID].get_participants():
                events_list.append(events[ID])
        if date:
            sorting.quicksort(events_list, sorting.compare_by_date)
        else:
            sorting.quicksort(events_list, sorting.compare_by_description)
        for event in events_list:
            list_string += str(event.get_id()) + "\t" + str(event.get_date()) + "\t" + str(event.get_time()) + "\t" + \
                           str(event.get_description()) + "\n"
        if list_string == "":
            list_string = "Person with the given ID isn't participating at any events"
        return list_string

    def report_20_percent(self):
        """
        Returns the list with the first 20% of events with the most participants
        :return: list_string
        :rtype: string
        """
        list_string = ""
        events_list = []
        events = self.__events_repo.get_events()
        for ID in events:
            events_list.append(events[ID])
        sorting.quicksort(events_list, sorting.compare_by_participants, True)
        count = 0.0
        limit = 0.2*len(events_list)
        for event in events_list:
            list_string += str(event.get_id()) + "\t" + str(event.get_description()) + "\t" + \
                           str(len(event.get_participants())) + " participants" + "\n"
            count += 1
            if count >= limit:
                break
        if list_string == "":
            list_string = "There are no events"
        return list_string
