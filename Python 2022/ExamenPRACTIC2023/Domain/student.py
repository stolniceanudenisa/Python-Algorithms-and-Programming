from dataclasses import dataclass


@dataclass
class Student:
    id_student: int
    nume_student: str
    numar_prezente: int
    nota: int

    def __str__(self):
        return f'Studentul cu id-ul: {self.id_student}, numele: {self.nume_student}, nr de prezente: {self.numar_prezente}, nota: {self.nota}'
