from Domain.animal import Animal


class RepoAnimal:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__animale = {}
        self.__sejur = {}

    def read_animale_from_file(self):
        """
        citeste din fisierul animale.txt, animalele si le introduce in dictionarul de animale
        :return: -
        """
        with open(self.__file_path, 'r') as f:
            lines = f.readlines()
            self.__animale.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_animal = int(parts[0])
                    nume = parts[1]
                    pret = int(parts[2])
                    specie = parts[3]
                    animal = Animal(id_animal, nume, pret, specie)
                    self.__animale[id_animal] = animal

    def get_all_repo(self):
        """
        returneaza lista de animale
        :return: rez: lista de animale
        """
        self.read_animale_from_file()
        animale = []
        for animal_id in self.__animale:
            animale.append(self.__animale[animal_id])
        return animale
