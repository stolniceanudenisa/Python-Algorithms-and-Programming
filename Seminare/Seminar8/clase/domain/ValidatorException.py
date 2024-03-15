class ValidatorException(Exception):

    def __init__(self, lista_mesaje_eroare):
        self.__lista_mesaje_eroare = lista_mesaje_eroare

    def __str__(self):
        mesaj = ""
        for eroare in self.__lista_mesaje_eroare:
            mesaj = mesaj + eroare + "\n"
        return mesaj