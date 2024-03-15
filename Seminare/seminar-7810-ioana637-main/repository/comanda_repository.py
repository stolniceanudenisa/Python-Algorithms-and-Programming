from domain.Comanda import Comanda


class OrderRepository:
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

    def create(self, order):
        '''
        Adds a new order.
        :param order: the given order
        :return: -
        :raises: KeyError if the id already exists
        '''
        order_id = order.id
        if order_id in self.__storage:
            raise KeyError('The order id already exists!')
        self.__storage[order_id] = order

    def read(self, order_id=None):
        '''
        Gets a order by id or all the orders
        :param order_id: optional, the order id
        :return: the list of orders or the order with the given id
        '''
        if order_id is None:
            return self.__storage.values()

        if order_id in self.__storage:
            return self.__storage[order_id]
        return None

    def update(self, order):
        '''
        Updates order.
        :param order: the order to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        order_id = order.id
        if order_id not in self.__storage:
            raise KeyError('There is no order with that id!')
        self.__storage[order_id] = order

    def delete(self, order_id):
        '''
        Deletes a order.
        :param order_id: the order id to delete.
        :return: -
        :raises KeyError: if no order with order_id
        '''
        if order_id not in self.__storage:
            raise KeyError('There is no order with that id!')
        del self.__storage[order_id]

    def clear(self):
        self.__storage.clear()


    def findByLocationId(self, location_id):
        pass

    def findByCarId(self, car_id):
        pass

