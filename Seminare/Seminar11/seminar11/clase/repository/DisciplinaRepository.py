from seminar11.clase.repository.Repository import Repository
from seminar11.clase.repository.RepositoryException import *


class DisciplinaRepository(Repository):

    def __init__(self):
        super().__init__()

    def get_disciplina_dupa_nume(self, nume_disciplina):
        for i in range(0, len(self._lista)):
            disciplina_curenta = self._lista[i]
            if disciplina_curenta.get_nume() == nume_disciplina:
                return disciplina_curenta
        return None