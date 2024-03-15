from Domain.Animal import Animal
from Repository.RepositoryAnimal import RepositoryAnimal


class RepositoryAnimalFile(RepositoryAnimal):
    def __init__(self, nume_fisier):
        RepositoryAnimal.__init__(self)
        self.nume_fisier = nume_fisier

    def load_from_file(self):
        with open(self.nume_fisier, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if line != '\n':
                    params = line.split(',')
                    id = int(params[0])
                    nume = params[1]
                    pret = int(params[2])
                    specie = params[3]
                    animal = Animal(id, nume, pret, specie)
                    self.container[id] = animal

    def write_to_file(self):
        with open(self.nume_fisier, "w") as f:
            animale = RepositoryAnimal.get_all(self)
            for key in animale:
                id = int(animale[key].get_id())
                nume = animale[key].get_nume()
                pret= int(animale[key].get_pret())
                specie = animale[key].get_specie()
                f.write(str(id) + ',' + nume + ',' + str(pret) + ',' + specie + '\n')

    def add(self,animal):
        self.load_from_file()
        RepositoryAnimal.add(self,animal)
        self.write_to_file()
    def delete(self,id):
        self.load_from_file()
        RepositoryAnimal.delete(self,id)
        self.write_to_file()
    def update(self,animal):
        self.load_from_file()
        RepositoryAnimal.update(self,animal)
        self.write_to_file()
    def find_by_id(self,id):
        self.load_from_file()
        return RepositoryAnimal.find_by_id(self,id)
    def get_all(self):
        self.load_from_file()
        return RepositoryAnimal.get_all(self)