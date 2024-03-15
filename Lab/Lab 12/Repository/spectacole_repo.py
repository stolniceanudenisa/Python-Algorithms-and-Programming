from Domain.entities import Spectacle


class SpectacoleRepo:
    def __init__(self, filename):
        """
        Initalizes the repo as an empty list
        :param filename: the name of the file where spectacles will be exported to
        """
        self.__filename = filename
        self.__repo = []
        self.load_from_file()

    def exists_in_repo(self, spectacle):
        """
        Verifies if a spectacle given by title exists in repo
        :param spectacle: the spectacles searched for
        :return: True if it exists, False otherwise
        """
        for elem in self.__repo:
            if spectacle.get_title() == elem.get_title():
                return True
        return False

    def add_to_repo(self, spectacle):
        """
        Adds a spectacle to repo
        :param spectacle: spectacle to add
        """
        self.__repo.append(spectacle)

    def modify_in_repo(self, spectacle):
        """
        Modifies a spectacle in repo
        :param spectacle: spectacle to modify
        """
        for i in range(len(self.__repo)):
            if spectacle.get_title() == self.__repo[i].get_title():
                self.__repo[i] = spectacle

    def load_from_file(self):
        """
        Loads data from file to repo
        Done when opening the app
        """
        spectacles = []
        try:
            file = open(self.__filename, "r")
        except IOError:
            print("Error accessing the file \"spectacles.txt\"")
            return
        lines = file.readlines()
        for row in lines:
            title, author, genre, duration = [token.strip() for token in row.split(",")]
            spectacle = Spectacle(title, author, genre, duration)
            spectacles.append(spectacle)
        file.close()
        self.__repo = spectacles

    def save_to_file(self, filename=None):
        """
        Saves data from repo to file, sorted by author and title
        Done whenever the repo is changed
        """
        if filename is None:
            name = self.__filename
        else:
            name = filename
        try:
            file = open(name, "w")
        except IOError:
            print("Error accessing the file \"spectacles.txt\"")
            return
        spectacles = self.__repo

        # sort by author and title
        for i in range(1, len(spectacles)):
            for j in range(i, 0, -1):
                if spectacles[j].get_artist() < spectacles[j-1].get_artist():
                    spectacles[j], spectacles[j-1] = spectacles[j-1], spectacles[j]
                elif spectacles[j].get_artist() == spectacles[j-1].get_artist() and \
                        spectacles[j].get_title() < spectacles[j - 1].get_title():
                    spectacles[j], spectacles[j - 1] = spectacles[j - 1], spectacles[j]

        for spectacle in spectacles:
            write_string = spectacle.get_title() + "," + spectacle.get_artist() + "," + spectacle.get_genre() + "," + \
                           str(spectacle.get_duration()) + '\n'
            file.write(write_string)
        file.close()

    def __len__(self):
        return len(self.__repo)
