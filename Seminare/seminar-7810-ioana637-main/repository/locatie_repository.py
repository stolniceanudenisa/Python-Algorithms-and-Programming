from domain.Car import Car
from domain.Locatie import Locatie


class LocatieRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}

    # metode CRUD
    # CRUD = Create
    #        Read
    #        Update
    #        Delete

    def create(self, locatie):
        '''
        Adds a new car.
        :param locatie: the given car
        :return: -
        :raises: KeyError if the id already exists
        '''
        locatie_id = locatie.id
        if locatie_id in self.__storage:
            raise KeyError('The location id already exists!')
        self.__storage[locatie_id] = locatie

    def read(self, locatie_id=None):
        '''
        Gets a car by id or all the cars
        :param locatie_id: optional, the car id
        :return: the list of cars or the car with the given id
        '''
        if locatie_id is None:
            return self.__storage.values()

        if locatie_id in self.__storage:
            return self.__storage[locatie_id]
        return None

    def update(self, locatie):
        '''
        Updates car.
        :param locatie: the car to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        locatie_id = locatie.id
        if locatie_id not in self.__storage:
            raise KeyError('There is no location with that id!')
        self.__storage[locatie_id] = locatie

    def delete(self, locatie_id):
        '''
        Deletes a car.
        :param locatie_id: the car id to delete.
        :return: -
        :raises KeyError: if no car with car_id
        '''
        if locatie_id not in self.__storage:
            raise KeyError('There is no location with that id!')
        del self.__storage[locatie_id]

    def clear(self):
        self.__storage.clear()

