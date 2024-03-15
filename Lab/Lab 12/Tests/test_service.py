import unittest
from Domain.entities import Spectacle
from Repository.spectacole_repo import SpectacoleRepo
from Service.spectacole_service import SpectacoleService


class SpectacoleServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = SpectacoleRepo("test_spectacles.txt")
        self.__service = SpectacoleService(self.__repo)

    def tearDown(self) -> None:
        file = open("test_spectacles.txt", "w")
        write_string = "Steve Aoki,Andrei,Concert,76\nNebojezubal,Izejofudafuj,Comedie,9225\nTRex,Kyocera,Concert,99"
        file.write(write_string)
        file.close()

    def test_adauga_spectacol(self):
        spect = Spectacle("Moara cu Noroc", "Ioan Slavici", "Comedie", 16)
        self.assertEqual(self.__repo.__len__(), 3)
        self.__service.add_spectacle(spect)
        self.assertEqual(self.__repo.__len__(), 4)

    def test_modifica_spectacol(self):
        spectacol = Spectacle("Steve Aoki", "Andrei", "Concert", 76)
        self.assertEqual(self.__service.modify_spectacle(spectacol), True)
        spectacol = Spectacle("Tulai Doamne", "Andrei", "Concert", 76)
        self.assertEqual(self.__service.modify_spectacle(spectacol), False)
