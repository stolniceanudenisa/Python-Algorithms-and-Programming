from Service.student_service import StudentService


class Console:
    def __init__(self, student_service: StudentService):
        self.__student_service = student_service

    def menu(self):
        print("""
        1. Afisare toti studentii.
        2. Adaugare student.
        3. Export bonus
        4. Update
        5. Delete
        x. Exit
        """)

    def run_ui(self):
        while True:
            self.menu()
            opt = input('Dati optiunea: ')
            if opt == '1':
                self.handle_afisare_studenti()
            elif opt == '2':
                self.handle_add_student()
            elif opt == '3':
                self.handle_export()
            elif opt == '4':
                self.handle_update()
            elif opt == '5':
                self.handle_delete()
            elif opt == 'x':
                break
            else:
                print('Comanda invalida. Reincercati.')

    def handle_afisare_studenti(self):
        studenti = self.__student_service.get_all_studenti()
        for student in studenti:
            print(student)

    def handle_add_student(self):
        try:
            ids = int(input('Dati id-ul studentului: '))
            nume = input('Dati numele studentului: ')
            nrprez = int(input('Dati nr de prezente ale studentului: '))
            nota = int(input('Dati nota studentului: '))
            self.__student_service.add_student(ids, nume, nrprez, nota)
            # print('Studentul a fost adaugat cu succes.')
            self.handle_afisare_studenti()
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(str(ve))

    def handle_export(self):
        p = int(input('Introduceti numarul p: '))
        b = int(input('Introduceti numarul b: '))
        filename = input('Dati numele fisierului unde se va exporta: ')
        self.__student_service.export(filename, p, b)
        print('Bonusurile au fost exportate cu succes!')

    def handle_update(self):
        try:
            ids = int(input('Dati id-ul studentului care se va modifica: '))
            nume = input('Dati numele nou studentului: ')
            nrprez = int(input('Dati nr de prezente noi ale studentului: '))
            nota = int(input('Dati nota noua a studentului: '))
            self.__student_service.update_student(ids, nume, nrprez, nota)
            self.handle_afisare_studenti()
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(str(ve))

    def handle_delete(self):
        try:
            ids = int(input('Dati id-ul studentului care se va sterge: '))
            self.__student_service.delete_student(ids)
            self.handle_afisare_studenti()
        except KeyError as ke:
            print(ke)
