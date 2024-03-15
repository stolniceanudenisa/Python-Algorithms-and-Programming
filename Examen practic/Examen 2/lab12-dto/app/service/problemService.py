"""

  author alex
  date 12/10/2022
  
"""
"""

  author alex
  date 12/10/2022

"""
from app.domeniu.problem import Problem
from app.repository.repositoryProblem import ProblemRepository


class ProblemService:
    def __init__(self, problemRepository: ProblemRepository):
        self.__problemRepository = problemRepository

    def getAllProblems(self):
        return self.__problemRepository.getAll()

    def addProblem(self, idProblem, problemDescription, problemDeadline):
        problem = Problem(idProblem, problemDescription, problemDeadline)
        self.__problemRepository.save(problem)

    def updateProblem(self, idProblem, newDescription, newDeadline):
        problem = Problem(idProblem, newDescription, newDeadline)
        self.__problemRepository.update(idProblem, problem)

    def deleteProblem(self, idProblem):
        self.__problemRepository.delete(idProblem)

    def findProblem(self, idProblem):
        return self.__problemRepository.getById(idProblem)



