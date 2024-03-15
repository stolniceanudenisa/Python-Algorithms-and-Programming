from dataclasses import dataclass


@dataclass
class Cafea:
    id_cafea: str
    nume_cafea: str
    tara_de_origine: str
    pret_cafea: float

    def __str__(self):
        return f'Cafeaua cu id-ul: {self.id_cafea}, ' \
               f'numele: {self.nume_cafea}, tara de origine: {self.tara_de_origine}, pretul: {self.pret_cafea}'
