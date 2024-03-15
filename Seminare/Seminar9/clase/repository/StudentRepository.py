from seminar10.clase.repository.Repository import Repository


class StudentRepository(Repository):

    def __init__(self):
        super().__init__()

    def get_student_by_id(self, id):
        for i in range(0, len(self._lista)):
            student_curent = self._lista[i]
            if student_curent.get_id() == id:
                return student_curent
        return -1