"""

  author alex
  date 12/12/2022
  
"""
from app.domeniu.assignment import Assignment
from app.repository.repositoryAss import AssRepository


class AssignmentFileRepository(AssRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__readFile()

    def save(self, assignment):
        super().save(assignment)
        self.__writeFile()

    def update(self, id, assignment):
        super().update(id, assignment)
        self.__writeFile()

    def delete(self, id):
        super().delete(id)
        self.__writeFile()

    def __readFile(self):
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idAss = int(line.split()[0])
                idStudent = int(line.split()[1])
                idProblem = int(line.split()[2])
                grade = int(line.split()[3])
                ass = Assignment(idAss, idStudent, idProblem, grade)
                self._allAssignments[idAss] = ass

    def __writeFile(self):
        with open(self.__filename, 'w') as f:
            for ass in self.getAll():
                f.write(f'{ass.id} {ass.idStudent} {ass.idProblem} {ass.grade}\n')