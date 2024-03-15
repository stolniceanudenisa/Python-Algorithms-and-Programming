"""

  author alex
  date 12/11/2022
  
"""
from app.domeniu.student import Student
from app.repository.repositoryStudent import StudentRepository


class StudentFileRepository(StudentRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__readFile()

    def save(self, student):
        super().save(student)
        self.__writeFile()

    def update(self, id, student):
        super().update(id, student)
        self.__writeFile()

    def delete(self, id):
        super().delete(id)
        self.__writeFile()

    def __readFile(self):
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                id = int(line.split()[0])
                name = line.split()[1]
                grup = int(line.split()[2])
                stud = Student(id, name, grup)
                self._allStudents[id] = stud

    def __writeFile(self):
        with open(self.__filename, 'w') as f:
            for stud in self.getAll():
                f.write(f'{stud.id} {stud.name} {stud.grup}\n')


