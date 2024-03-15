from seminar11.clase.domain.Entitate import Entitate


class Student(Entitate):
    def __init__(self, id, nume):
        '''
        Metoda ce initializeaza un Student cu valorile dorite pentru atributele id si nume
        :param id: id-ul studentului (unic)
        :param nume: numele studentului
        '''
        super().__init__(id)
        self.__id = id
        self.__nume = nume

    #-----------------------------------getteri
    def get_nume(self):
        return self.__nume

    #-----------------------------------setteri
    def set_nume(self, nume_nou):
        self.__nume = nume_nou

    #-----------------------------------metoda similara cu to_string de la Lab4-6
    def __str__(self):
        '''
        Metoda care reprezinta obiectul clasei Student ca un sir de caractere formatat frumos
        :return: sir de caractere care reprezinta obiectul nostru Student
        '''
        return "Student " + str(self.get_id()) + " : " + self.get_nume()