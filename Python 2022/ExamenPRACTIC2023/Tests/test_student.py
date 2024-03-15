from Domain.student import Student
from Domain.student_validator import StudentValidator
from Repository.student_file_repository import StudentFileRepo
from Service.student_service import StudentService


class Teste:
    def __init__(self):
        self.run_all_tests()
        print('Testele au trecut!')

    def run_all_tests(self):
        self.test_domain()
        self.test_repo()
        self.test_service()

    def test_domain(self):
        pass

    def test_repo(self):
        student = Student(60, 'alex velea', 5, 6)
        assert student.id_student == 60
        assert student.nume_student == 'alex velea'
        assert student.numar_prezente == 5
        assert student.nota == 6

        student_repo = StudentFileRepo("Tests/test_student.txt")
        studenti = student_repo.get_all()

        student = Student(61, 'alex velea', 5, 6)
        student_repo.add(student)

        # try:
        #     carte_repo.add(carte)
        #     assert False  # exista deja cartea cu id '1'
        # except KeyError:
        #     ...

        assert len(studenti) == 3

        assert student_repo.get_by_id(61) is not None

        # student_repo.update(Student(61, 'ema ema', 9, 9))
        # assert student_repo.get_by_id(61).id_student == 61
        # assert student_repo.get_by_id(61).nume_student == 'ema ema'
        # assert student_repo.get_by_id(61).numar_prezente == 0
        # assert student_repo.get_by_id(61).nota == 0

        try:
            student_repo.update(Student(9999, 'eeee eeee', 5, 6))
            assert False
        except KeyError:
            ...
        #
        # student_repo.delete(61)
        # assert len(studenti) == 0

        try:
            student_repo.delete('777')
            assert False  # nu exista cartea cu id 777 pe care sa o stergem
        except KeyError:
            ...

    def test_service(self):
        student_repo = StudentFileRepo("Tests/test_student.txt")
        student_validator = StudentValidator()
        student_service = StudentService(student_repo, student_validator)

        studenti = student_service.get_all_studenti()
        assert len(studenti) == 2

        student_service.add_student(99, 'ela bella', 10, 10)
        student_service.update_student(99, 'ana maria', 8, 8)

        try:
            student_service.update_student(100, 'eeeee fffff', 2, 2)
            assert False
        except KeyError:
            ...

        # student_service.delete_student(99)
