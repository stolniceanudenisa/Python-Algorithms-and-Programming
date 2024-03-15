from domeniu.angajat import Angajat
from repository.repository import Repository


class FileAngajatRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, angajat):
        super().adauga(angajat)
        self.__writeFile()

    def modifica(self, angajat):
        super().modifica(angajat)
        self.__writeFile()

    def sterge(self, idAngajat):
        super().sterge(idAngajat)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idAngajat = line.split()[0]
                nume = line.split()[1]
                angajat = Angajat(idAngajat, nume)
                self._entitati[idAngajat] = angajat

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for angajat in self.getAll():
                f.write(f'{angajat.getIdEntitate()} {angajat.getNume()}\n')