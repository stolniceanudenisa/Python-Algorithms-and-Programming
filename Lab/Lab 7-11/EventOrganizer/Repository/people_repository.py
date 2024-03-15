
class PeopleRepo:
    def __init__(self):
        # {ID_person : Person}
        self.__people = {}

    def __len__(self):
        return len(self.__people)

    def get_people(self):
        """
        Return the dictionary with people from repo
        :return: self.__people
        :rtype: dictionary {ID_person : Person}
        """
        return self.__people

    def set_people(self, people):
        """
        Replaces the current list of people with the given list
        :param people: the dictionary of people that will overwrite self.__people
        :type people: dictionary {ID_person : Person}
        """
        self.__people = people

    def add(self, person):
        """
        Adds a person to the repo
        :param person: person to add
        :type person: Person
        """
        self.__people[person.get_id()] = person

    def find(self, person_id):
        """
        Search person by ID
        :param person_id: wanted ID
        :type person_id: int
        :return: the person with the given ID or None
        :rtype: Person
        """
        if person_id in self.__people:
            return self.__people[person_id]
        else:
            return None

    def delete(self, person_id):
        """
        Deletes a person from repo
        :param person_id: wanted ID
        :type person_id: int
        """
        del self.__people[person_id]

    def modify(self, person):
        """
        Modifies a person in repo
        :param person: modified person, identified by ID
        :type person: Person
        """
        self.__people[person.get_id()] = person

    def increment_events(self, person_id):
        """
        Increments the number of events a person with the given ID takes part in
        :param person_id: wanted ID
        :type person_id: int
        """
        self.__people[person_id].increment_events()

    def decrement_events(self, person_id):
        """
        Decrements the number of events a person with the given ID takes part in
        :param person_id: wanted ID
        :type person_id: int
        """
        self.__people[person_id].decrement_events()

    def get_events_count(self, person_id):
        """
        Returns the number of events the person with the given ID takes part in
        :param person_id: wanted ID
        :type person_id: int
        :return: the number of events the person takes part in
        :rtype: int
        """
        return self.__people[person_id].get_events_count()
