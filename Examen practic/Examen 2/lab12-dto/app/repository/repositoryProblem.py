"""

  author alex
  date 12/10/2022
  
"""
class ProblemRepository:
    def __init__(self):
        self._allProblems = {}

    def getAll(self):
        return list(self._allProblems.values())

    def getById(self, id):
        if id in self._allProblems:
            return self._allProblems[id]
        return None

    def save(self, problem):
        self._allProblems[problem.id] = problem

    def delete(self, id):
        self._allProblems.pop(id)

    def update(self, id, problem):
        self._allProblems[id] = problem
