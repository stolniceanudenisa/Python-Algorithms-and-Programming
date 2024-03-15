from repository.repository_exception import RepositoryException


class CarRepository:
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

    def create(self, car):
        '''
        Adds a new car.
        :param car: the given car
        :return: -
        :raises: KeyError if the id already exists
        '''
        car_id = car.id
        if car_id in self.__storage:
            raise RepositoryException('The car id already exists!')
        self.__storage[car_id] = car

    def read(self, car_id=None):
        '''
        Gets a car by id or all the cars
        :param car_id: optional, the car id
        :return: the list of cars or the car with the given id
        '''
        if car_id is None:
            return self.__storage.values()

        if car_id in self.__storage:
            return self.__storage[car_id]
        return None

    def update(self, car):
        '''
        Updates car.
        :param car: the car to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        car_id = car.id
        if car_id not in self.__storage:
            raise RepositoryException('There is no car with that id!')
        self.__storage[car_id] = car

    def delete(self, car_id):
        '''
        Deletes a car.
        :param car_id: the car id to delete.
        :return: -
        :raises KeyError: if no car with car_id
        '''
        if car_id not in self.__storage:
            raise RepositoryException('There is no car with that id!')
        del self.__storage[car_id]

    def clear(self):
        self.__storage.clear()


