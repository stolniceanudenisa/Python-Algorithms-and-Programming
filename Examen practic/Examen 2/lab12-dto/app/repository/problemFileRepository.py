"""

  author alex
  date 12/12/2022
  
"""
from app.domeniu.problem import Problem
from app.repository.repositoryProblem import ProblemRepository


class ProblemFileRepository(ProblemRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__readFile()

    def save(self, problem):
        super().save(problem)
        self.__writeFile()

    def update(self, id, problem):
        super().update(id, problem)
        self.__writeFile()

    def delete(self, id):
        super().delete(id)
        self.__writeFile()

    def __readFile(self):
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                id = int(line.split()[0])
                description = line.split()[1]
                deadline = int(line.split()[2])
                prob = Problem(id, description, deadline)
                self._allProblems[id] = prob

    def __writeFile(self):
        with open(self.__filename, 'w') as f:
            for prob in self.getAll():
                f.write(f'{prob.id} {prob.description} {prob.deadline}\n')