class Spectacle:
    def __init__(self, title, artist, genre, duration):
        self.__title = title
        self.__artist = artist
        self.__genre = genre
        self.__duration = duration

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_genre(self):
        return self.__genre

    def get_duration(self):
        return self.__duration

    def set_title(self, value):
        self.__title = value

    def set_artist(self, value):
        self.__artist = value

    def set_genre(self, value):
        self.__genre = value

    def set_duration(self, value):
        self.__duration = value
