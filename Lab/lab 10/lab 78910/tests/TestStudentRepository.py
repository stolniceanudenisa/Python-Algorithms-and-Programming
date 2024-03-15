from domeniu.student import Student
from repository.repository import Repository


def testAdaugaStudentRepository():
    studentRepository = Repository()
    student = Student("1", "ana", "311", "")

    studentRepository.adauga(student)

    studenti = studentRepository.getAll()
    assert len(studenti) == 1
    assert studenti[0].getIdStudent() == "1"

    try:
        studentRepository.adauga(student)
        assert False
    except KeyError:
        ...

def testModificaStudentRepository():
    studentRepository = Repository()
    student = Student("1", "ana", "311")
    studentNou1 = Student("1", "paul", "411")
    studentNou2 = Student("2", "ion", "311" )
    studentRepository.adauga(student)

    studentRepository.modifica(student.getIdEntitate(), studentNou1)

    studenti = studentRepository.getAll()
    assert studenti[0].getNume() == "paul"

    try:
        studentRepository.modifica(student.getIdEntitate(), studentNou2)
        assert False
    except KeyError:
        ...

def testStergeStudentRepository():
    studentRepository = Repository()
    student = Student("1", "ana", "311")
    studentRepository.adauga(student)

    studentRepository.sterge("1")

    assert len(studentRepository.getAll()) == 0

    try:
        studentRepository.sterge("!")
        assert False
    except KeyError:
        ...