"""

  author alex
  date 12/10/2022
  
"""
class AssRepository:
    def __init__(self):
        self._allAssignments = {}

    def getAll(self):
        return list(self._allAssignments.values())

    def getById(self, id):
        if id in self._allAssignments:
            return self._allAssignments[id]
        return None

    def save(self, ass):
        self._allAssignments[ass.id()] = ass

    def delete(self, id):
        self._allAssignments.pop(id)

    def update(self, id, ass):
        self._allAssignments[id] = ass
