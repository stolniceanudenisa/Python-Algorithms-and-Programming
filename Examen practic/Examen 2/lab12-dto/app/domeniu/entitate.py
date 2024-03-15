"""

  author alex
  date 12/10/2022
  
"""
from dataclasses import dataclass

'''
class Entitate:
    def __init__(self, idEntitate):
        self.__idEntitate = idEntitate

    def getIdEntitate(self):
        return self.__idEntitate

    def setIdEntitate(self, idEntitate):
        self.__idEntitate = idEntitate
'''

@dataclass
class Entitate:
    id: int