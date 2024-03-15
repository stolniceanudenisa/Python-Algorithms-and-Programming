from seminar10.clase.domain.Disciplina import Disciplina
from seminar10.clase.domain.DisciplinaValidator import DisciplinaValidator
from seminar10.clase.domain.ValidatorException import ValidatorException
from seminar10.clase.repository.RepositoryException import *


class UI:

    def __init__(self, student_controller, disciplina_controller, inscriere_controller):
        self.__student_controller = student_controller
        self.__disciplina_controller = disciplina_controller
        self.__inscriere_controller = inscriere_controller

        self.__disciplina_validator = DisciplinaValidator()

    def meniu(self):
        meniu = ""
        meniu += "1. Tipareste toti studentii\n"
        meniu += "2. Adauga student\n"
        meniu += "3. Tipareste toate disciplinele\n"
        meniu += "4. Adauga disciplina\n"
        meniu += "5. Sterge disciplina\n"
        meniu += "6. Modifica disciplina\n"
        meniu += "7. Tipareste toate inscrierile\n"
        meniu += "8. Adauga inscriere (inscrie student la disciplina)\n"
        meniu += "9. Lista studenti si notele lor la o disciplina data ordonati dupa nota, dupa nume\n"
        meniu += "10. Primii N studenti ordonati dupa media la toate disciplinele (N citit de la tastatura)\n"
        meniu += "11. Lista nume studenti inscrisi la o anumita disciplina\n"
        meniu += "0. Iesire\n"
        return meniu

    def program(self):
        ruleaza = True
        while ruleaza == True:
            meniul_meu = self.meniu()
            print(meniul_meu)
            comanda = input("Introduceti comanda:")
            if comanda == "1":
                self.ui_tipareste_studenti()
            elif comanda == "2":
                self.ui_adauga_student()
            elif comanda == "3":
                self.ui_tipareste_discipline()
            elif comanda == "4":
                self.ui_adauga_disciplina()
            elif comanda == "5":
                self.ui_sterge_disciplina()
            elif comanda == "6":
                self.ui_modifica_disciplina()
            elif comanda == "7":
                self.ui_tipareste_inscrieri()
            elif comanda == "8":
                self.ui_adauga_inscriere()
            elif comanda == "9":
                self.ui_studenti_la_disciplina_ordonati_nota_nume()
            elif comanda == "10":
                self.ui_studenti_ordonati_medie()
            elif comanda == "11":
                self.ui_studenti_inscrisi_la_disciplina()
            elif comanda == "0":
                ruleaza = False
            else:
                print("Comanda gresita! Reincercati!")

    def ui_adauga_student(self):
        try:
            id = int(input("Introduceti id:"))
            nume = input("Introduceti nume:")
            self.__student_controller.adauga(id, nume)
        except ValueError:
            print("Date gresite! Reincercati!")
        except DuplicateIDException as de:
            print(de)

    def ui_tipareste_studenti(self):
        studenti = self.__student_controller.get_all()
        if len(studenti) == 0:
            print("Lista de studenti e goala!")
        for student in studenti:
            print(student)

    def ui_tipareste_discipline(self):
        discipline = self.__disciplina_controller.get_all()
        if len(discipline) == 0:
            print("Lista de discipline e goala!")
        for disciplina in discipline:
            print(disciplina)

    def ui_adauga_disciplina(self):
        try:
            id = int(input("Introduceti id:"))
            nume = input("Introduceti nume:")
            self.__disciplina_validator.valideaza_nume(nume)
            profesor = input("Introduceti profesor:")
            self.__disciplina_validator.valideaza_nume(profesor)
            self.__disciplina_controller.adauga(id, nume, profesor)
        except ValueError:
            print("Date gresite! Reincercati!")
        except DuplicateIDException as de:
            print(de)
        except ValidatorException as ve:
            print(ve)

    def ui_sterge_disciplina(self):
        try:
            id = int(input("Introduceti id-ul disciplinei pe care doriti sa o stergeti:"))
            if self.__inscriere_controller.exista_inscriere_disciplina(id) == True:
                print("Exista deja inscrieri la acesta disciplina, deci ea nu poate fi stearsa!")
                print("Stergeti fortat? (se va efectua stergerea --in cascada-- si vor si sterse, pe langa disciplina, si toate inscrierile studentilor la aceasta disciplina)")
                accept = input("da/nu:")
                if accept == "da":
                    self.__inscriere_controller.sterge_disciplina_cascada(id)
            else:
                self.__disciplina_controller.sterge(id)
        except ValueError:
            print("Date gresite! Reincercati!")
        except InexistentIDException as ie:
            print(ie)

    def ui_modifica_disciplina(self):
        try:
            id = int(input("Introduceti id-ul disciplinei pe care doriti sa o modificati:"))
            nume_nou = input("Introduceti nume nou:")
            profesor_nou = input("Introduceti profesor nou:")
            self.__disciplina_controller.modifica(id, nume_nou, profesor_nou)
        except ValueError:
            print("Date gresite! Reincercati!")
        except InexistentIDException as ie:
            print(ie)

    def ui_tipareste_inscrieri(self):
        inscrieri = self.__inscriere_controller.get_all()
        if len(inscrieri) == 0:
            print("Lista de inscrieri e goala!")
        for inscriere in inscrieri:
            print(inscriere)

    def ui_adauga_inscriere(self):
        try:
            id = int(input("Introduceti id:"))
            student_id = int(input("Introduceti ID Student:"))
            disciplina_id = int(input("Introduceti ID Disciplina:"))
            nota = int(input("Introduceti nota:"))
            self.__inscriere_controller.adauga(id, student_id, disciplina_id, nota)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)
        except DuplicateIDException as de:
            print(de)

    def ui_studenti_la_disciplina_ordonati_nota_nume(self):
        try:
            disciplina = input("Numele disciplinei:")
            studenti = self.__inscriere_controller.returneaza_studenti_la_disciplina_ordonati_nota_nume(disciplina)
            print(studenti)
        except KeyError as ke:
            print(ke)

    def ui_studenti_ordonati_medie(self):
        try:
            nr_maxim_studenti_afisati = int(input("Cati dintre cei mai buni studenti vreti sa afisati:"))
            studenti = self.__inscriere_controller.returneaza_studenti_ordonati_medie(nr_maxim_studenti_afisati)
            print(studenti)
        except:
            print("Date gresite! Reincercati!")

    def ui_studenti_inscrisi_la_disciplina(self):
        try:
            nume_disciplina = input("Nume disciplina:")
            lista_studenti = self.__inscriere_controller.studenti_inscrisi_la_disciplina(nume_disciplina)
            print(lista_studenti)
        except:
            print("Date incorecte! Reincercati!")