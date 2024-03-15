from Service.sessionservice import sessionService
from Service.gradeservice import gradeService


class Console:
    def __init__(self, sessionService: sessionService,
                 gradeService: gradeService):
        self.sessionservice = sessionService
        self.gradeservice = gradeService

    @staticmethod
    def printMenu():
        print("""
        To choose an option just type the associated number/letter
        1.Add grade
        2.Add session
        3.Show session by number of students
        4.Show session with grades from a given name
        5.Export JSON:
        6. SHow all grades
        7. Show all sessions
        m. Menu
        x. Exit""")

    def runConsole(self):
        stop = False
        while not stop:
            self.printMenu()
            command = input("Choose command: ")
            if command == '1':
                self.handle_add_grade()
            elif command == '2':
                self.handle_add_session()
            elif command == '3':
                self.handle_session_students()
            elif command == '4':
                self.handle_session_name()
            elif command == '5':
                self.handle_export_json()
            elif command == '6':
                self.handle_show_all(self.gradeservice.get_all_grade())
            elif command == '7':
                self.handle_show_all(self.sessionservice.get_all_session())
            elif command == 'm':
                self.printMenu()
            elif command == 'x':
                stop = True
            else:
                print("Invalid command")

    def handle_add_session(self):
        try:
            nr_students = int(input("Enter number of students of session: "))
            grades = []
            stop = False
            print("Enter grades IOs and when you're done just type 'x'")
            while not stop:
                grade = input("Enter grade or 'x' to stop: ")
                if grade == 'x':
                    stop = True
                else:
                    grades.append(grade)
            self.sessionservice.add_session(nr_students, grades)
        except ValueError as ve:
            print("Validation Error: ", ve)
        except Exception as ex:
            print("Error: ", ex)

    def handle_show_session(self):
        try:
            ID = input("Enter the ID: ")
            needed_object = self.sessionservice.get_session(ID)
            if needed_object is None:
                print("No item found with the given ID")
            else:
                print(needed_object)
        except Exception as ex:
            print("Error:", ex)

    def handle_add_grade(self):
        try:
            grade_value = int(input("Grade value: "))
            name = input("Name of examenee: ")
            self.gradeservice.add_grade(grade_value, name)
        except ValueError as ve:
            print("ValIDation Error: ", ve)
        except Exception as ex:
            print("Error: ", ex)

    def handle_show_grade(self):
        try:
            ID = input("Enter the ID: ")
            needed_object = self.gradeservice.get_grade(ID)
            if needed_object is None:
                print("No item found with the given ID")
            else:
                print(needed_object)
        except Exception as ex:
            print("Error:", ex)

    @staticmethod
    def handle_show_all(objects: list):
        if len(objects):
            for obj in objects:
                print(obj)
        else:
            print("Empty!")

    def handle_session_students(self):
        try:
            sessions = self.sessionservice.session_by_students()
            for session in sessions:
                print(session)
        except Exception as ex:
            print("Error: ", ex)

    def handle_session_name(self):
        try:
            name = input("Enter examinee name: ")
            sessions = self.sessionservice.session_by_examinee(name)
            for session in sessions:
                print(session)
        except Exception as ex:
            print("Error: ", ex)

    def handle_export_json(self):
        try:
            filename = input("Enter file name: ")
            self.sessionservice.export_json(filename)
        except Exception as ex:
            print("Error: ", ex)
