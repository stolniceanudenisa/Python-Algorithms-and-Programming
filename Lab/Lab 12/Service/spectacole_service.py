import string
import random
from Domain.entities import Spectacle


class SpectacoleService:
    def __init__(self, spectacole_repo):
        self.__repo = spectacole_repo

    def add_spectacle(self, spectacle):
        """
        Adds a spectacle
        :param spectacle: spectacole to add
        :return: True if operation is succesful, False otherwise
        """
        if self.__repo.exists_in_repo(spectacle):
            return False

        self.__repo.add_to_repo(spectacle)
        self.__repo.save_to_file()
        return True

    def modify_spectacle(self, spectacle):
        """
        Modifies the spectacle with the same title
        :param spectacle: spectacle to modify
        :return: True if operation is succesful, False otherwise
        """
        if not self.__repo.exists_in_repo(spectacle):
            return False

        self.__repo.modify_in_repo(spectacle)
        self.__repo.save_to_file()
        return True

    def generate_spectacles(self, count):
        """
        Generates a number of spectacles
        :param count: number of spectacles to generate
        :return spec_string: a string with the generated spectacles to print them
        """
        for i in range(count):
            genres = ["Comedy", "Concert", "Ballet", "Other"]
            genre = genres[random.randint(0, 3)]
            duration = random.randint(1, 10000)
            # generate title
            length = random.randint(9, 12)
            letter = random.randint(0, 1)  # first letter, 0 vowel, 1 consonant
            title = ""
            vowels = "aeiou"
            for j in range(length):
                if letter == 0:
                    pos = random.randint(0, 4)
                    title += vowels[pos]
                else:
                    x = random.choice(string.ascii_lowercase)
                    while x in vowels:
                        x = random.choice(string.ascii_lowercase)
                    title += x
                letter = (letter+1) % 2
            title = title.capitalize()
            # generate artist
            length = random.randint(9, 12)
            letter = random.randint(0, 1)  # first letter, 0 vowel, 1 consonant
            artist = ""
            for j in range(length):
                if letter == 0:
                    pos = random.randint(0, 4)
                    artist += vowels[pos]
                else:
                    x = random.choice(string.ascii_lowercase)
                    while x in vowels:
                        x = random.choice(string.ascii_lowercase)
                    artist += x
                letter = (letter+1) % 2
            artist = artist.capitalize()
            spectacle = Spectacle(title, artist, genre, duration)
            self.add_spectacle(spectacle)

    def export_spectacles(self, filename):
        """
        Exports spectacles
        """
        self.__repo.save_to_file(filename)
