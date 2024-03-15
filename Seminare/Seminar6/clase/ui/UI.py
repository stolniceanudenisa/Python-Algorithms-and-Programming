class UI:

    def __init__(self, student_controller, disciplina_controller):
        self.__student_controller = student_controller
        self.__disciplina_controller = disciplina_controller

    def meniu(self):
        meniu = ""
        meniu += "1. Tipareste toti studentii\n"
        meniu += "2. Adauga student\n"
        meniu += "3. Tipareste toate disciplinele\n"
        meniu += "4. Adauga disciplina\n"
        meniu += "5. Sterge disciplina\n"
        meniu += "6. Modifica disciplina\n"
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
        except KeyError as ke:
            print(ke)

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
            profesor = input("Introduceti profesor:")
            self.__disciplina_controller.adauga(id, nume, profesor)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def ui_sterge_disciplina(self):
        try:
            id = int(input("Introduceti id-ul disciplinei pe care doriti sa o stergeti:"))
            self.__disciplina_controller.sterge(id)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def ui_modifica_disciplina(self):
        try:
            id = int(input("Introduceti id-ul disciplinei pe care doriti sa o modificiati:"))
            nume_nou = input("Introduceti nume nou:")
            profesor_nou = input("Introduceti profesor nou:")
            self.__disciplina_controller.modifica(id, nume_nou, profesor_nou)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)
