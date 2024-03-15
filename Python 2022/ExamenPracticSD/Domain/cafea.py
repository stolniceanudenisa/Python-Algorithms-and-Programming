from dataclasses import dataclass


@dataclass
class Cafea:
    """
    Clasa pentru obiect de tip cafea.
    id_cafea: int, id-ul cafelei
    nume_cafea: str, numele
    tara_de_origine: str, tara
    pret_cafea: float, pretul
   `"""
    id_cafea: int
    nume_cafea: str
    tara_de_origine: str
    pret_cafea: float

    def __str__(self):
        return f'Cafeaua cu id-ul: {self.id_cafea}, numele: {self.nume_cafea}, tara de origine: {self.tara_de_origine}, pretul: {self.pret_cafea}'
