"""

  author alex
  date 12/10/2022
  
"""
from app.domeniu.entitate import Entitate
from dataclasses import dataclass
'''
class Problem(Entitate):
    def __init__(self, idProblem, description, deadline):
        super().__init__(idProblem)
        self.__description = description
        self.__deadline = deadline

    def getDescription(self):
        return self.__description

    def getDeadline(self):
        return self.__deadline

    def setDescription(self, description):
        self.__description = description

    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return f"Numar problema {self.getIdEntitate()}, descriere: {self.__description}, deadline: {self.__deadline} zile"
'''

@dataclass
class Problem:
    id: int
    description: str
    deadline: int

    def __str__(self):
        return f"Numar problema {self.id}, descriere: {self.description}, deadline: {self.deadline} zile"