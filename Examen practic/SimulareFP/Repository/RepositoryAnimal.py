class RepositoryAnimal:
    def __init__(self):
        self.container={}
    def add(self,animal):
        """
        Functie care introduce un animal in hotel.

        """
        self.container[animal.get_id()]=animal
    def delete(self,id):
        """
        Functie care sterge un animal din baza de date a hotelului(dupa id)
        :param id: int
        :return: Baza de date modificata
        """
        self.container.pop(id)
    def update(self,animal):
        """
        Functie care modifica atributele unui animal
        :param animal: -
        :return: Animalul modificat
        """
        self.container[animal.get_id()] = animal
    def find_by_id(self,id):
        """
        Functie care returneaza animalul cu id-ul dorit.
        :param id: int
        :return: Animalul cu id-ul dorit
        """
        return self.container[int(id)]
    def get_all(self):
        """
        Functie care returneaza toate animalele din hotel.
        """
        return self.container
    def __len__(self):
        """
        Functie care returneaza cate animale sunt cazate in hotel(la momentul actual)
        :return: Numarul de animale
        """
        return len(self.container)