from seminar9.clase.domain.Disciplina import Disciplina


class DisciplinaController:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        '''
        Metoda care returneaza lista din repository
        :return: lista din repository
        '''
        return self.__repository.get_all()

    def adauga(self, id, nume, profesor):
        '''
        Metoda care adauga o noua disciplina in lista (din repository)
        :param id:
        :param nume:
        :param profesor:
        :return:
        '''
        disciplina = Disciplina(id, nume, profesor)
        self.__repository.adauga(disciplina)

    def sterge(self, id):
        '''
        Metoda care sterge o disciplina din lista (din repository)
        :param id:
        :return:
        '''
        self.__repository.sterge(id)

    def modifica(self, id, nume_nou, profesor_nou):
        '''
        Metoda care modifica numele si profesorul disciplinei cu id-ul dat
        :param id:
        :param nume_nou:
        :param profesor_nou:
        :return:
        '''
        self.__repository.modifica(id, nume_nou, profesor_nou)
