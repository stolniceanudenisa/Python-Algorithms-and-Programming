class StudentRepository:

    def __init__(self):
        self.__lista_studenti = []

    def get_all(self):
        '''
        Metoda care returneaza lista studentilor
        :return: lista studenti
        '''
        return self.__lista_studenti

    def adauga(self, student):
        '''
        Metoda care adauga un student in lista
        :param student:
        :return:
        Arunca o eroare daca id-ul studentului pe care vrem sa il introducem exista deja in lista. Eroarea e tratata in UI.
        '''
        if self.gaseste_student_dupa_id(student.get_id()) != -1:
            raise KeyError("Exista deja un student cu acest id!")
        else:
            self.__lista_studenti.append(student)

    def gaseste_student_dupa_id(self, id):
        '''
        Metoda care returneaza pozitia in lista de studenti a unui student, dupa id
        :param id: id-ul studentului pe care il cautam
        :return: pozitia studentului in lista, daca el exista in lista de studenti; -1, altfel
        '''
        for i in range(0, len(self.__lista_studenti)):
            student_curent = self.__lista_studenti[i]
            if student_curent.get_id() == id:
                return i
        return -1