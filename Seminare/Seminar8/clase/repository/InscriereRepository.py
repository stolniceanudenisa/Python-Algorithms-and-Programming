class InscriereRepository:

    def __init__(self, student_repository, disciplina_repository):
        self.__lista_inscrieri = []
        #in InscriereRepository pastram referinte spre StudentRepository si DisciplinaRepository
        self.__student_repository = student_repository
        self.__disciplina_repository = disciplina_repository

    def get_all(self):
        return self.__lista_inscrieri

    def adauga(self, inscriere):
        id = inscriere.get_id()
        if self.gaseste_inscriere_dupa_id(id) != -1:
            # nu adaugam inscrierea daca exista deja o inscriere cu acest id
            raise KeyError("Inscrierea cu acest id exista deja!")
        else:
            student_id = inscriere.get_student_id()
            disciplina_id = inscriere.get_disciplina_id()
            #aici vom folosi faptul ca am initializat si referinte spre StudentRepository si DisciplinaRepository
            #verificam ca student_id sa fie id-ul unui student existent in StudentRepository
            #de aceea avem nevoie de referinta spre StudentRepository, ca sa putem avea acces la lista de studenti, sa facem verificarea
            #procedam la fel si pentru disciplina_id
            #daca oricare dintre student_id si disciplina_id nu sunt id-urile unui Student / Discipline din repository-urile corespunzatoare, nu facem adaugarea
            if self.__student_repository.gaseste_student_dupa_id(student_id) == -1 or self.__disciplina_repository.gaseste_disciplina_dupa_id(disciplina_id) == -1:
                raise KeyError("Studentul sau disciplina inscrierii nu exista!")
            elif self.gaseste_inscriere_dupa_student_id_si_disciplina_id(student_id, disciplina_id) != -1:
                #daca exista deja in lista de inscrieri o inscriere cu acelasi student_id si disciplina_id, nu facem adaugarea
                raise KeyError("Studentul este deja inscris la aceasta disciplina!")
            else:
                #daca totul e in regula, adaugam inscrierea in lista
                self.__lista_inscrieri.append(inscriere)

    def gaseste_inscriere_dupa_id(self, id):
        '''
        Metoda care gaseste o inscriere in lista de inscrieri, dupa id inscriere
        :param id: id-ul inscrierii cautate
        :return: pozitia unui obiectului de tip inscriere cu id-ul dat in self.__lista_inscrieri;
                -1 daca nu exista
        '''
        for i in range(0, len(self.__lista_inscrieri)):
            inscriere_curenta = self.__lista_inscrieri[i]
            if inscriere_curenta.get_id() == id:
                return i
        return -1

    def gaseste_inscriere_dupa_student_id_si_disciplina_id(self, student_id, disciplina_id):
        '''
        Metoda care gaseste o inscriere in lista de inscrieri, dupa id student si id disciplina
        :param student_id:
        :param: disciplina_id:
        :return: pozitia unui obiectului de tip inscriere cu id student si id disciplina date in self.__lista_inscrieri;
                -1 daca nu exista
        '''
        for i in range(0, len(self.__lista_inscrieri)):
            inscriere_curenta = self.__lista_inscrieri[i]
            if inscriere_curenta.get_student_id() == student_id and inscriere_curenta.get_disciplina_id() == disciplina_id:
                return i
        return -1

    def exista_inscriere_disciplina(self, disciplina_id):
        '''
        Metoda care verifica daca exista inscrieri la disciplina cu id-ul dat
        :param disciplina_id: id-ul disciplinei cautate
        :return: True, daca exista o inscriere la disciplina cu id-ul dat; False altfel
        '''
        for i in range(0, len(self.__lista_inscrieri)):
            inscriere_curenta = self.__lista_inscrieri[i]
            if inscriere_curenta.get_disciplina_id() == disciplina_id:
                return True
        return False

    def sterge_inscrieri_disciplina(self, id_disciplina):
        '''
        Metoda care sterge din lista de inscrieri toate inscrierile la disciplina cu id-ul dat
        :param id_disciplina:
        :return:
        '''
        i = 0
        while i < len(self.__lista_inscrieri):
            inscriere_curenta = self.__lista_inscrieri[i]
            if inscriere_curenta.get_disciplina_id() == id_disciplina:
                self.__lista_inscrieri.pop(i)
                i = i - 1
            i = i + 1
