import unittest

from Business.Service import Service
from Domain.Animal import Animal
from Repository.RepositoryAnimalFile import RepositoryAnimalFile


class Teste(unittest.TestCase):

    def __goleste_fisier(self, nume_fisier):
        with open(nume_fisier, "w") as f:
            pass

    def tearDown(self):
        pass

    def teste_repo_ap(self):
        """
        Functie de test pentru RepositoryAnimalFile
        """
        nume_fisier = "Testare/teste_hotel_animal1.txt"
        repo_animal = RepositoryAnimalFile(nume_fisier)
        self.__goleste_fisier(nume_fisier)

        id1 = 1
        nume = "Oscar"
        pret = 1000
        specie = "Caine"
        animal1 = Animal(id1, nume, pret, specie)

        self.assertTrue(len(repo_animal) == 0)
        repo_animal.add(animal1)
        self.assertTrue(len(repo_animal) == 1)

        id2 = 2
        nume = "Tietu"
        pret = 250
        specie = "Pisica"
        animal2 = Animal(id2, nume, pret, specie)

        repo_animal.add(animal2)
        self.assertTrue(len(repo_animal) == 2)

        id = 3
        nume = "Jerry"
        pret = 100
        specie = "Soarece"
        animal3 = Animal(id, nume, pret, specie)

        repo_animal.add(animal3)
        self.assertTrue(len(repo_animal) == 3)
        repo_animal.delete(id)
        self.assertTrue(len(repo_animal) == 2)

        self.assertTrue(repo_animal.find_by_id(id1)!=animal3)
        self.assertTrue(repo_animal.find_by_id(id2)!=animal1)

    def test_service_animal(self):
        """
        Functie de test pentru Service
        """
        nume_fisier = "Testare/teste_hotel_animale2.txt"
        repo_animal = RepositoryAnimalFile(nume_fisier)
        service = Service(repo_animal)
        self.__goleste_fisier(nume_fisier)

        id = 1
        nume = "Oscar"
        pret = 1000
        specie = "Caine"
        animal1 = Animal(id, nume, pret, specie)

        self.assertTrue(len(repo_animal) == 0)
        service.add(animal1)
        self.assertTrue(len(repo_animal) == 1)

        id = 2
        nume = "Tietu"
        pret = 250
        specie = "Pisica"
        animal2 = Animal(id, nume, pret, specie)

        service.add(animal2)
        self.assertTrue(len(repo_animal) == 2)

        id = 3
        nume = "Jerry"
        pret = 100
        specie = "Soarece"
        animal3 = Animal(id, nume, pret, specie)

        service.add(animal3)
        self.assertTrue(len(repo_animal) == 3)
        service.delete(id)
        self.assertTrue(len(repo_animal) == 2)

        self.assertTrue(service.pret_total("Oscar", 2) == 2000)
        self.assertTrue(service.pret_total("Tietu", 10) == 2500)

        self.assertTrue(animal1.get_id()==1)
        self.assertTrue(animal1.get_nume()=="Oscar")
        self.assertTrue(animal1.get_pret()==1000)
        self.assertTrue(animal1.get_specie()=="Caine")



