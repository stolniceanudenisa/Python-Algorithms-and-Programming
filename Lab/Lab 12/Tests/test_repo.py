import unittest
from Domain.entities import Spectacle
from Repository.spectacole_repo import SpectacoleRepo


class SpectacoleRepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = SpectacoleRepo("test_spectacles.txt")

    def test_adauga_spectacol_in_repo(self):
        spect = Spectacle("Moara cu Noroc", "Ioan Slavici", "Comedie", 16)
        self.assertEqual(self.__repo.__len__(), 3)
        self.__repo.add_to_repo(spect)
        self.assertEqual(self.__repo.__len__(), 4)

    def test_modifica_spectacol_in_repo(self):
        spect = Spectacle("Steve Aoki", "Andrei", "Concert", 76)
        self.assertEqual(self.__repo.exists_in_repo(spect), True)
        spect = Spectacle("Steve Aoki", "Andrei", "Concert", 78)
        self.__repo.modify_in_repo(spect)
