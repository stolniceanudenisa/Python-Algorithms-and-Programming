class UI:

    def __init__(self, controller):
        self.__controller = controller

    def meniu(self):
        meniu = ""
        meniu += "1. Tipareste toti studentii\n"
        meniu += "2. Adauga student\n"
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
            elif comanda == "0":
                ruleaza = False
            else:
                print("Comanda gresita! Reincercati!")

    def ui_adauga_student(self):
        try:
            id = int(input("Introduceti id:"))
            nume = input("Introduceti nume:")
            self.__controller.adauga(id, nume)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def ui_tipareste_studenti(self):
        studenti = self.__controller.get_all()
        if len(studenti) == 0:
            print("Lista de studenti e goala!")
        for student in studenti:
            print(student)
