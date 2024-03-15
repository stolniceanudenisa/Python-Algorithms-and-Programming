"""

  author alex
  date 12/10/2022
  
"""
from dataclasses import dataclass

from app.domeniu.entitate import Entitate
'''
class Student(Entitate):
    def __init__(self, idStudent, name, grup):
        super().__init__(idStudent)
        self.__name = name
        self.__grup = grup

    def getName(self):
        return self.__name

    def getGrup(self):
        return self.__grup

    def setName(self, name):
        self.__name = name

    def setGrup(self, grup):
        self.__grup = grup

    def __str__(self):
        return f"id: {self.entitate()}, nume: {self.__name}, grupa: {self.__grup}"
'''

@dataclass
class Student:
    id: int
    name: str
    grup: int

    def __str__(self):
        return f"student cu id {self.id}, nume {self.name} si grupa {self.grup}"


