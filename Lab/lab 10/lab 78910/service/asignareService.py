from domeniu.asignare import Asignare
from domeniu.exceptii.duplicateError import DuplicateError
from repository.repository import Repository


class AsignareService:
    def __init__(self, asignareRepository: Repository, studentiRepository: Repository, problemeRepository: Repository):
        self.__asignareRepository = asignareRepository
        self.__studentiRepository = studentiRepository
        self.__problemaRepository = problemeRepository

    def getAllAsignari(self):
        '''
        returneaza lista de asignari
        :return: o lista de obiecte de tipul Asignare
        '''
        return self.__asignareRepository.getAll()

    def adaugaAsignare(self, idAsignare, idStudent, idProblemaLaborator, nota):
        '''
        adauga o asignare
        :param idAsignare: string
        :param idStudent:   string
        :param idProblemaLaborator:    string
        :param nota:    string
        :return:
        '''
        if self.__studentiRepository.getById(idStudent) is None:
            raise KeyError("Nu exista un student cu id-ul dat")
        if self.__problemaRepository.getById(idProblemaLaborator) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")

        asignari = self.__asignareRepository.getAll()
        for asignare in asignari:
            if asignare.getIdStudent() == idStudent and asignare.getIdProblema() == idProblemaLaborator:
                raise DuplicateError("Studentul este deja inscris la problema data")

        asignare = Asignare(idAsignare, idStudent, idProblemaLaborator, nota)
        self.__asignareRepository.adauga(asignare)

    def stergeAsignare(self, idAsignare):
        '''
        sterge o asignare care are id-ul idStudent si id-ul idProblemaLaborator
        :param idStudent: string
        :param idProblemaLaborator:
        :return:
        '''
        self.__asignareRepository.sterge(idAsignare)

    def modificaAsignare(self, idAsignare, idStudentNou, idProblemaLaboratorNoua, notaNoua):
        '''
        functia modifica toate datele despre o asignare cu id-ul dat
        :param idStudentNou: string
        :param idStudentNou: string
        :param idProblemaLaboratorNoua: string
        :param notaNoua: string
        :return:
        '''
        if self.__studentiRepository.getById(idStudentNou) is None:
            raise KeyError("Nu exista un student cu id-ul dat")
        if self.__problemaRepository.getById(idProblemaLaboratorNoua) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")

        asignareNoua = Asignare(idAsignare, idStudentNou, idProblemaLaboratorNoua, notaNoua)
        self.__asignareRepository.modifica(asignareNoua)

    def cautareAsignare(self, idAsignare):
        '''
        functia cauta si afiseaza asignarea cu id-ul dat
        :param idAsignare: string
        :return:
        '''
        return self.__asignareRepository.cauta(idAsignare)

    def ordonare(self, idProblema, param):
        """

        :param idProblema:
        :param criteriuSortare:
        :return:
        """
        #if self.__problemaRepository.getById(idProblema) is None:
            #raise KeyError("Nu exista o problema cu id-ul dat")
        asignari = self.__asignareRepository.getAll()
        studenti = self.__studentiRepository.getAll()
        lista = []
        for asignare in asignari:
            if asignare.getIdProblema() == idProblema:
                for student in studenti:
                    if student.getIdEntitate() == asignare.getIdStudent():
                        lista.append([student.getNume(), asignare.getNota()])
                        #lista.append(student.getNume())
                        #lista[index] = lista[index] + " " + asignare.getNota()
                        #index += 1
        if param == "1":
            lista.sort()
        elif param == "2":
            lista.sort(key= lambda x: x[1])
        else:
            raise KeyError("Sortare inexistenta")
        if lista == []:
            return "Problema cu id-ul introdus nu este asignata niciunui student"

        return lista


    def getStudentiCuMedieSubCinci(self):
        listaNote = []
        listaAsign = self.getAllAsignari()
        listaStud = self.__studentiRepository.getAll()
        for student in listaStud:
            nrNote = 0
            sumNote = 0
            for asignare in listaAsign:
                if asignare.getIdStudent() == student.getIdEntitate():
                    sumNote = sumNote + int(asignare.getNota())
                    nrNote += 1
            if(nrNote != 0):
                listaNote.append(sumNote/nrNote)
        rez = []
        i = 0
        for student in listaStud:
            j = 0
            for nota in listaNote:
                if i == j:
                    if(nota < 5):
                        rez.append((student.getNume(),nota))
                    break
                j += 1
            i += 1
        return rez