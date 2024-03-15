from Domain.entities import Event


class EventsRepo:
    def __init__(self):
        # {ID_event : Event}
        self.__events = {}

    def get_events(self):
        """
        Returns all the events from Repo
        """
        return self.__events

    def __len__(self):
        return len(self.__events)

    def set_events(self, events):
        """
        Replaces the current list of events with the given list
        :param events: the dictionary of events that will replace self.__events
        :type events: {ID_event : event}
        """
        self.__events = events

    def add(self, event):
        """
        Adds the event to the repo
        :param event: the event to add
        :type event: Event
        """
        self.__events[event.get_id()] = event

    def find(self, event_id):
        """
        Search event by ID
        :param event_id: wanted ID
        :type event_id: int
        :return: the event with the given ID or None
        :rtype: Event
        """
        if event_id in self.__events:
            return self.__events[event_id]
        else:
            return None

    def delete(self, event_id):
        """
        Deletes an event from repo
        :param event_id: wanted ID
        :type event_id: int
        """
        del self.__events[event_id]

    def modify(self, event):
        """
        Modifies an event in repo
        :param event: modified event, identified by ID
        :type event: Event
        """
        self.__events[event.get_id()] = event
