import unittest
from Repository.events_repository import EventsRepo
from Domain.entities import *
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__events_repo = EventsRepo()

    def test_repo(self):
        # add
        date1 = datetime.strptime("1911/1/1", "%Y/%m/%d")
        time1 = datetime.strptime("14:27", "%H:%M")
        event1 = Event(1, date1, time1, "Bazooka")
        date2 = datetime.strptime("2111/6/9", "%Y/%m/%d")
        time2 = datetime.strptime("7:54", "%H:%M")
        event2 = Event(6, date2, time2, "Lolipop")
        date3 = datetime.strptime("1961/5/1", "%Y/%m/%d")
        time3 = datetime.strptime("13:58", "%H:%M")
        event3 = Event(1, date3, time3, "Bazinga")
        self.assertEqual(self.__events_repo.__len__(), 0)
        self.__events_repo.add(event1)
        self.assertEqual(self.__events_repo.__len__(), 1)
        # find
        self.assertEqual(self.__events_repo.find(1), event1)
        self.assertEqual(self.__events_repo.find(1337), None)
        # modify
        self.assertEqual(self.__events_repo.find(1), event1)
        self.__events_repo.modify(event3)
        self.assertEqual(self.__events_repo.find(1), event3)
        # delete
        self.assertEqual(self.__events_repo.__len__(), 1)
        self.__events_repo.delete(1)
        self.assertEqual(self.__events_repo.__len__(), 0)
        # set
        self.assertEqual(self.__events_repo.find(6), None)
        self.__events_repo.set_events({event2.get_id(): event2})
        self.assertEqual(self.__events_repo.find(6), event2)
        # get
        events = self.__events_repo.get_events()
        self.assertEqual(events[event2.get_id()], event2)
        self.assertEqual(len(events), self.__events_repo.__len__())
