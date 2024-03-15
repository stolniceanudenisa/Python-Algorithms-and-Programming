class DuplicateError(Exception):
    def __init__(self, mesaj):
        self.__mesaj = mesaj

    def __str__(self):
        return f'DuplicateError: {self.__mesaj}'