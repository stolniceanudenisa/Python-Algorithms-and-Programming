class Entitate:

    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id_nou):
        self.__id = id_nou

    def __str__(self):
        return "ID: " + str(self.get_id()) + "\n"