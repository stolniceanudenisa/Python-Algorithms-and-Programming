from abc import ABC


class Entity(ABC):
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
