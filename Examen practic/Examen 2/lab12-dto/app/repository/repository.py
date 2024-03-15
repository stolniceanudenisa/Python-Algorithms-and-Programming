"""

  author alex
  date 12/10/2022
  
"""
class Repository:
    def __init__(self):
        self._allEntitati = {}

    def getAll(self):
        return list(self._allEntitati.values())

    def getById(self, id):
        if id in self._allEntitati:
            return self._allEntitati[id]
        return None

    def save(self, entitate):
        self._allEntitati[entitate.getIdEntitate()] = entitate

    def delete(self, id):
        self._allEntitati.pop(id)

    def update(self, id, entitate):
        self._allEntitati[id] = entitate
