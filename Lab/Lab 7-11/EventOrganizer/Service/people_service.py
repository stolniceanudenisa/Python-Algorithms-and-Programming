import random
import string
from Domain.entities import Person
from Repository.people_repository import PeopleRepo
from Service import sorting


class PeopleService:
    def __init__(self, people_repo):
        """
        Initializes service
        :param people_repo: the repository we use to store people
        :type people_repo: PeopleRepo
        """
        self.__people_repo = people_repo

    def replace_people(self, people):
        """
        Replaces the people in repo with those in people
        :param people: people to replace with
        :type people: {ID_person : Person}
        """
        self.__people_repo.set_people(people)

    def get_people(self):
        """
        Returns all people in repo
        :return: people:
        :rtype: {ID_event : Person}
        """
        return self.__people_repo.get_people()

    def add_person(self, person):
        """
        Adds person
        :param person: person to add in repo
        :type person: Person
        :return: True if the person was added, False if a person with the same ID already exists
        :rtype: bool
        """
        if self.__people_repo.find(person.get_id()) is not None:
            return False
        self.__people_repo.add(person)
        return True

    def delete_person(self, person_id):
        """
        Deletes the person with the given ID
        :return: True if the person was deleted, False if a person with the given ID deosn't exist
        :rtype: bool
        """
        if self.__people_repo.find(person_id) is None:
            return False
        self.__people_repo.delete(person_id)
        return True

    def modify_person(self, person):
        """
        Modifies person
        :param person: person to modify
        :type person: Person
        :return: True if the person was modified, False if a person with the same ID doesn't exist
        :rtype: bool
        """
        if self.__people_repo.find(person.get_id()) is not None:
            return False
        self.__people_repo.modify(person)
        return True

    def list_people(self):
        """
        Returns a list of people or the message "The list of people is empty"
        :return: list_string - the list of people from repo
        :rtype: string
        """
        list_string = ""
        people = self.__people_repo.get_people()
        for ID in people:
            list_string += str(ID) + "\t" + str(people[ID].get_name()) + "\t" + str(people[ID].get_address()) + "\n"
        if list_string == "":
            list_string = "The list of people is empty"
        else:
            list_string = "ID\t\tName\t\tAddress\n" + list_string
        return list_string

    def generate_people(self):
        """
        Generates a random number of people (let's assume Polish =)
        """
        count = random.randint(1, 10)
        for i in range(count):
            first_length = random.randint(3, 10)
            first = ""
            last_length = random.randint(5, 8)
            last = ""
            address_length = random.randint(5, 15)
            address = ""
            # Generates an unique ID
            person_id = random.randint(1, 10000)
            while self.__people_repo.find(person_id) is not None:
                person_id = random.randint(1, 10000)
            # Generates first name
            for j in range(first_length):
                first += random.choice(string.ascii_lowercase)
            first = first.capitalize()
            # Generates last name
            for j in range(last_length):
                last += random.choice(string.ascii_lowercase)
            last = last.capitalize()
            # Composes the name
            name = first + " " + last
            # Generates address
            for j in range(address_length):
                address += random.choice(string.ascii_lowercase)
            address = address.capitalize()
            # Adds the person to repo
            person = Person(str(person_id), name, address)
            self.add_person(person)

    def search_people(self, name):
        """
        Returns a list of people whose names contain name or the message "There are no people with the given name"
        :param name: name to search for
        :type name: string
        :return: list_string
        :rtype: string
        """
        list_string = ""
        people = self.__people_repo.get_people()
        for ID in people:
            if people[ID].get_name().find(name) != -1:
                list_string += str(ID) + "\t" + str(people[ID].get_name()) + "\t" + str(people[ID].get_address()) + "\n"
        if list_string == "":
            list_string = "There are no people with the given name"
        return list_string

    def get_participant(self, person_id):
        """
        Returns person from repo by given ID
        :param person_id: ID of the participant
        :type person_id: int
        :return person: person searched for or None if they do not exist
        :rtype person: Person
        """
        person = self.__people_repo.find(person_id)
        return person

    def increment_events(self, person_id):
        """
        Increments the count of events the person with the given ID is taking part in
        :param person_id: ID of the person
        :type person_id: string
        """
        self.__people_repo.increment_events(person_id)

    def decrement_events(self, people):
        """
        Decrements the count of events the people with the given IDs are taking part in
        :param people: people's IDs
        :type people: [string, string, ...]
        """
        for ID in people:
            self.__people_repo.decrement_events(ID)

    def report_most_active_people(self):
        """
        Returns the list with the people participating in most events
        :return: list_string
        :rtype: string
        """
        list_string = ""
        people = self.__people_repo.get_people()
        count = 0
        people_list = []
        for ID in people:
            people_list.append(people[ID])
        sorting.gnomesort(people_list, sorting.compare_by_events_count, True)
        for person in people_list:
            list_string += str(person.get_id()) + "\t" + str(person.get_name()) + "\t" + str(person.get_address())  \
                           + "\t" + str(person.get_events_count()) + " events" + "\n"
            count += 1
            if count == 5:
                break
        if list_string == "":
            list_string = "The list of people is empty"
        return list_string
