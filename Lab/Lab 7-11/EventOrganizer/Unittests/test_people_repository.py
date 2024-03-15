import unittest


from EventOrganizer.Domain.entities import Person
from EventOrganizer.Repository.people_repository import PeopleRepo


class PeopleRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._people_repo = PeopleRepo()

    def test_add(self):
        pers1 = Person(1, "Steve Aoki", "Manastur 69")
        self.assertEqual(self._people_repo.__len__(), 0)
        self._people_repo.add(pers1)
        self.assertEqual(self._people_repo.__len__(), 1)

    def test_get_people(self):
        pers1 = Person(1, "Steve Aoki", "Manastur 69")
        pers2 = Person(2, "Danny DeVito", "Hollywood")
        people = {
            1: pers1,
            2: pers2
        }
        self._people_repo.add(pers1)
        self._people_repo.add(pers2)
        self.assertEqual(self._people_repo.get_people(), people)

    def test_set_people(self):
        pers1 = Person(1, "Steve Aoki", "Manastur 69")
        pers2 = Person(2, "Danny DeVito", "Hollywood")
        self._people_repo.add(pers1)
        self._people_repo.add(pers2)
        pers3 = Person(3, "6ix9ine", "Jail")
        pers4 = Person(4, "Don Gus", "Aragaz")
        people = {
            3: pers3,
            4: pers4
        }
        self._people_repo.set_people(people)
        self.assertEqual(self._people_repo.get_people(), people)

    def test_find(self):
        pers1 = Person(1, "Steve Aoki", "Manastur 69")
        self._people_repo.add(pers1)
        self.assertEqual(self._people_repo.find(1), pers1)
        self.assertEqual(self._people_repo.find(2), None)

    def test_delete(self):
        pers1 = Person(1, "Steve Aoki", "Manastur 69")
        pers2 = Person(2, "Danny DeVito", "Hollywood")
        self._people_repo.add(pers1)
        self._people_repo.add(pers2)
        self.assertEqual(self._people_repo.__len__(), 2)
        self._people_repo.delete(2)
        self.assertEqual(self._people_repo.__len__(), 1)
        self.assertEqual(self._people_repo.find(2), None)

    def test_modify(self):
        person = Person(1, "Steve Aoki", "Manastur 69")
        self._people_repo.add(person)
        new_person = Person(1, "Mr Nothing", "Nowhere")
        self._people_repo.modify(new_person)
        self.assertEqual(self._people_repo.find(1).get_name(), "Mr Nothing")
        self.assertEqual(self._people_repo.find(1).get_address(), "Nowhere")

    def test_increment_events(self):
        person = Person(1, "Steve Aoki", "Manastur 69")
        self._people_repo.add(person)
        self._people_repo.increment_events(1)

        self.assertEqual(self._people_repo.find(1).get_events_count(), 1)

    def test_decrement_events(self):
        person = Person(1, "Steve Aoki", "Manastur 69")
        self._people_repo.add(person)
        self._people_repo.increment_events(1)
        self._people_repo.increment_events(1)
        self.assertEqual(self._people_repo.find(1).get_events_count(), 2)
        self._people_repo.decrement_events(1)
        self.assertEqual(self._people_repo.find(1).get_events_count(), 1)

    def test_get_events_count(self):
        person = Person(1, "Steve Aoki", "Manastur 69")
        self._people_repo.add(person)
        self._people_repo.increment_events(1)
        self._people_repo.increment_events(1)
        self.assertEqual(self._people_repo.get_events_count(1), 2)
