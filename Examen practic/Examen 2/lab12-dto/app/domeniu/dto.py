"""

  author alex
  date 12/22/2022
  
"""
from dataclasses import dataclass

@dataclass
class StudentNota:
    nume: str
    nota: list[float]

    def __repr__(self):
        return "nume: {}, nota: {}".format(self.nume, self.nota)


class StudentNotaAssembler:
    @staticmethod
    def createDTO(student, nota):
        nume = student.getNume()
        nota = [float(entitate.getNota()) for entitate in nota]
        return StudentNota(nume, nota)