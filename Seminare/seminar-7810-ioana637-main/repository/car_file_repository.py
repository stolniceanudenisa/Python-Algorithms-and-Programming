import pickle

from repository.car_repository import CarRepository


class CarFileRepository(CarRepository):
    '''
    Repository for storing data in file
    '''

    def __init__(self, filename):
        '''
        Creates an in memory repository.
        '''
        super().__init__()
        self.__filename = filename or 'cars.pkl'

    # metode CRUD
    # CRUD = Create
    #        Read
    #        Update
    #        Delete


    def __load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def __save_to_file(self):
        try:
            with open(self.__filename, 'wb') as f_write:
                pickle.dump(self.__storage, f_write)
        except Exception:
            self.__storage.clear()

    def create(self, car):
        '''
        Adds a new car.
        :param car: the given car
        :return: -
        :raises: KeyError if the id already exists
        '''
        self.__load_from_file()
        super().create(car)
        self.__save_to_file()

    def read(self, car_id=None):
        '''
        Gets a car by id or all the cars
        :param car_id: optional, the car id
        :return: the list of cars or the car with the given id
        '''
        self.__load_from_file()
        return super().read(car_id)

    def update(self, car):
        '''
        Updates car.
        :param car: the car to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        self.__load_from_file()
        super().update(car)
        self.__save_to_file()

    def delete(self, car_id):
        '''
        Deletes a car.
        :param car_id: the car id to delete.
        :return: -
        :raises KeyError: if no car with car_id
        '''
        self.__load_from_file()
        super().delete(car_id)
        self.__save_to_file()

    def clear(self):
        super().clear()
        self.__save_to_file()
