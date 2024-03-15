from seminar9.clase.domain.Inscriere import Inscriere

class InscriereController:

    def __init__(self, inscriere_repository, student_repository, disciplina_repository):
        self.__inscriere_repository = inscriere_repository
        self.__student_repository = student_repository
        self.__disciplina_repository = disciplina_repository

    def get_all(self):
        return self.__inscriere_repository.get_all()

    def adauga(self, id, student_id, disciplina_id, nota):
        inscriere = Inscriere(id, student_id, disciplina_id, nota)
        self.__inscriere_repository.adauga(inscriere)

    def exista_inscriere_disciplina(self, disciplina_id):
        return self.__inscriere_repository.exista_inscriere_disciplina(disciplina_id)

    def returneaza_studenti_la_disciplina_ordonati_nota_nume(self, nume_disciplina):
        '''
        Metoda ce returneaza studentii de la o disciplina cautata cu notele la acea disciplina, ordonati crescator dupa note, apoi (daca doi studenti au aceeasi nota) dupa numele studentului
        :param nume_disciplina: numele disciplinei cautate
        :return: dictionar sortat dupa note (apoi, in caz de note egale, dupa nume student) cu numele studentilor si notele lor la disciplina cautata
        '''
        disciplina = self.__disciplina_repository.get_disciplina_dupa_nume(nume_disciplina)
        if disciplina == -1:
            raise KeyError("Disciplina cu acest nume nu exista!")
        else:
            id_disciplina = disciplina.get_id()
            dictionar_student_note = self.get_studenti_cu_note(id_disciplina)
            #dictionar_student_note are forma {"NumeStudent":nota_student, ...}
            #exemplu: {"Sara":9, "Dana":10, "Andrei":10} -> {"Sara":9, "Andrei":10, "Dana":10}
            #in functia predefinita sorted() d[0] se refera la "NumeStudent", iar d[1] se refera la nota_student
            dictionar_sortat = sorted(dictionar_student_note.items(), key=lambda d:(d[1],d[0]))
            return dictionar_sortat

    def get_studenti_cu_note(self, id_disciplina):
        '''
        Metoda ce returneaza un dictionar care mapeaza numele studentului si nota obtinuta la disciplina cu id-ul dat
        :param id_disciplina: id-ul disciplinei cautate
        :return: un dictionar care mapeaza numele studentului si nota obtinuta la disciplina cu id-ul dat
        '''
        # vom salva intr-un dictionar numele si nota fiecarui student, ex: {nume_student1: nota_student1, nume_student2: nota_student2, ...}
        dictionar_student_nota = {} #in acest dictionar cheile vor fi numele studentilor, iar valorile vor fi notele
        inscrieri = self.get_all() #luam lista de inscrieri a studentilor la discipline
        for inscriere in inscrieri: #o parcurgem inscriere cu inscriere
            if inscriere.get_disciplina_id() == id_disciplina: #daca am gasit o inscriere la disciplina cautata
                student_id = inscriere.get_student_id() #luam id-ul studentului inscris la acea disciplina
                student = self.__student_repository.get_student_by_id(student_id) # in student_repository, cautam obiectul student cu acel id si il returnam
                nume_student = student.get_nume() #am avut nevoie de obiectul student, ca sa putem lua numele studentului -> acum nume_student este numele studentului inscris la disciplina cautata
                nota = inscriere.get_nota() #luam din inscriere nota studentului la acea disciplina
                dictionar_student_nota[nume_student] = nota #adaugam in dictionar la cheia aferenta numelui studentului, nota lui la disciplina cautata
        return dictionar_student_nota

    def returneaza_studenti_ordonati_medie(self, nr_maxim_studenti_afisati):
        '''
        Metoda ce returneaza cei mai buni studenti, ordonati dupa mediile la toate materiile
        :param nr_maxim_studenti_afisati:
        :return: cei mai buni <nr_maxim_studenti_afisati> studenti, ordonati dupa mediile la toate materiile
        '''
        dictionar_student_medie = {} #vom tine un dictionar care va mapa numele studentului si media notelor lui la toate materiile
        dictionar_student_numar_note = {} #si un dictionar care va mapa numele studentului si numarul materiilor la care a primit nota
        #pentru ca initial in dictionar_student_medie vom face suma notelor studentilor la toate materiile
        #iar apoi ne vom folosi de dictionar_student_numar_note pentru a calcula media corect pentru fiecare student(vom imparti suma notelor studentului la numarul de note primite de el)
        inscrieri = self.get_all() #luam toate inscrierile
        for inscriere in inscrieri: #le parcurgem una cate una
            student_id = inscriere.get_student_id()  #luam din inscriere id-ul fiecarui student
            student = self.__student_repository.get_student_by_id(student_id)  #in student_repository, cautam obiectul student cu acel id si il returnam
            nume_student = student.get_nume()  #am avut nevoie de obiectul student, ca sa putem lua numele studentului -> acum nume_student este numele studentului de la inscrierea curenta
            nota = inscriere.get_nota()  #luam din inscriere nota studentului
            if nume_student not in dictionar_student_medie: #daca numele studentului nu apare inca in dictionar_student_medie
                dictionar_student_medie[nume_student] = nota #il adaugam dandu-i ca valoare nota curenta
                dictionar_student_numar_note[nume_student] = 1 #marcam in dictionar_student_numar_note ca studentul cu acest nume are nota la o materie
            else: #daca numele studentului apare deja in dictionar_student_medie
                dictionar_student_medie[nume_student] = dictionar_student_medie[nume_student] + nota #adunam la suma notelor noua nota gasita
                dictionar_student_numar_note[nume_student] = dictionar_student_numar_note[nume_student] + 1 #adunam la numarul notelor studentului inca 1

        for nume_student in dictionar_student_medie: #pentru fiecare student din dictionar_student_medie
            dictionar_student_medie[nume_student] = dictionar_student_medie[nume_student] / dictionar_student_numar_note[nume_student] #facem media notelor studentului impartind suma notelor la numarul lor
            #pentru asta ne folosim de ambele dictionare create: dictionar_student_medie care avea inainte suma notelor studentului si dictionar_student_numar_note care ne arata numarul notelor studentului

        #sortam dictionarul dictionar_student_medie in functie de medie in ordine inversa si returnam doar primele nr_maxim_studenti_afisati elemente
        dictionar_ordonat_dupa_medie = sorted(dictionar_student_medie.items(), key=lambda d:(d[1]), reverse=True)[:nr_maxim_studenti_afisati]
        return dictionar_ordonat_dupa_medie

    def studenti_inscrisi_la_disciplina(self, nume_disciplina):
        '''
        Metoda ce returneaza lista studentilor inscrisi la disciplina data
        :param nume_disciplina:
        :return: lista studenti
        '''
        lista_studenti = []
        lista_inscrieri = self.__inscriere_repository.get_all()
        for inscriere in lista_inscrieri:
            id_disciplina = inscriere.get_disciplina_id()
            disciplina = self.__disciplina_repository.get_disciplina_by_id(id_disciplina)
            if disciplina.get_nume() == nume_disciplina:
                student_id = inscriere.get_student_id()
                student = self.__student_repository.get_student_by_id(student_id)
                nume = student.get_nume()
                lista_studenti.append(nume)
        return lista_studenti

    def sterge_disciplina_cascada(self, id_disciplina):
        '''
        Metoda care sterge fortat o disciplina din lista de discipline.
        Adica pe langa faptul ca sterge disciplina din lista de discipline, sterge si toate inscrierile studenilor la acea disciplina
        :param id_disciplina:
        :return:
        '''
        self.__inscriere_repository.sterge_inscrieri_disciplina(id_disciplina)
        self.__disciplina_repository.sterge(id_disciplina)