from Domain.Sejur import Sejur
from Repository.RepositoryAnimal import RepositoryAnimal


class Service:
    def __init__(self,repoAnimal:RepositoryAnimal):
        self.repoAnimal=repoAnimal
    def add(self,animal):
        """
        Functie care introduce un animal in hotel.
        """
        return self.repoAnimal.add(animal)
    def delete(self,id):
        """
        Functie care sterge un animal din baza de date a hotelului
        :param id: int
        :return: Baza de date modificata
        """
        return self.repoAnimal.delete(id)
    def update(self,animal):
        """
        Functie care modifica un animal din baza de date a hotelului
        :param animal: -
        :return: Baza de date modificata
        """
        return self.repoAnimal.update(animal)
    def find_by_id(self,id):
        """
        Functie care returneaza animalul cu id-ul dorit.
        :param id: int
        :return: Animalul cu id-ul dorit
        """
        return self.repoAnimal.find_by_id(id)
    def get_all(self):
        """
        Functie care returneaza toate animalele din hotel
        :return: Animalele
        """
        return self.repoAnimal.get_all()
    def print_all(self):
        """
        Functie care printeaza toate animalele din hotel
        """
        animale=self.repoAnimal.get_all()
        for animal in animale:
            print(animale[animal])
    def find_by_specie(self,specie):
        """
        Functie care afiseaza toate animalele de o specie anume.
        :param specie: str
        """
        animale=self.repoAnimal.get_all()
        ok=0
        for animal in animale:
            if animale[animal].get_specie().strip()==specie.strip():
               ok=1
        if ok==0:
            print("Nu exista animale din aceasta specie!")
        else:
            for animal in animale:
                if animale[animal].get_specie().strip() == specie.strip():
                    print(animale[animal])
    def pret_total(self,nume,nr_zile):
        """
        Functie care calculeaza pretul total al sejurului unui animal din hotel
        :param nume: str
        :param nr_zile: int
        :return: Pret_total
        """
        animale=self.repoAnimal.get_all()
        ok=0
        for animal in animale:
            if animale[animal].get_nume().strip() == nume.strip():
                ok=1
        if ok==0:
            return -1
        else:
            for animal in animale:
                if animale[animal].get_nume().strip() == nume.strip():
                    var=animale[animal].get_pret()
        rez=int(var)*int(nr_zile)
        sejur=Sejur(nume,nr_zile)
        return rez

