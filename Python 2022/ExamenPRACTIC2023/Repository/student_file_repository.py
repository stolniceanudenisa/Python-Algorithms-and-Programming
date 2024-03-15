from Domain.student import Student


class StudentFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def read_file(self):
        lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            self.__storage.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(',')
                    ids = parts[0]
                    nume = parts[1]
                    nrprez = parts[2]
                    nota = parts[3]
                    student = Student(str(ids), nume, int(nrprez), int(nota))
                    self.__storage[ids] = student
                    lista.append(student)
        return lista

    def write_file(self):
        with open(self.__filename, "w") as f:
            studenti = self.__storage
            for key in studenti:
                ids = studenti[key].id_student
                nume = studenti[key].nume_student
                nrprez = studenti[key].numar_prezente
                nota = studenti[key].nota
                f.write(str(ids) + ',' + nume + ',' + str(nrprez) + ',' + str(nota) + '\n')

    def get_all(self):
        self.read_file()
        return self.__storage.values()

    def add(self, student: Student):
        self.read_file()
        if self.get_by_id(student.id_student) is not None:
            raise KeyError(f'Exista deja studentul cu id-ul: {student.id_student}.')
        self.__storage[student.id_student] = student
        self.write_file()

    def get_by_id(self, id_student):
        if id_student in self.__storage:
            return self.__storage[id_student]
        return None

    def update(self, student: Student):
        self.read_file()
        if self.get_by_id(student.id_student) is None:
            raise KeyError(f'Nu exista studentul cu id-ul: {student.id_student} care sa se modifice.')
        self.__storage[student.id_student] = student
        self.write_file()

    def delete(self, id_student):
        self.read_file()
        if self.get_by_id(id_student) is None:
            raise KeyError(f'Nu exista studentul cu id-ul: {id_student} care sa se stearga.')
        del self.__storage[id_student]
        self.write_file()
