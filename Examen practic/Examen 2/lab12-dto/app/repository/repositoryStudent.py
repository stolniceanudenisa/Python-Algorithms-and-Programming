"""

  author alex
  date 12/10/2022
  
"""

class StudentRepository:
    def __init__(self):
        self._allStudents = {}

    def getAll(self):
        return list(self._allStudents.values())

    def getById(self, id):
        if id in self._allStudents:
            return self._allStudents[id]
        return None

    def save(self, student):
        self._allStudents[student.id] = student

    def delete(self, id):
        self._allStudents.pop(id)

    def update(self, id, student):
        self._allStudents[id] = student
