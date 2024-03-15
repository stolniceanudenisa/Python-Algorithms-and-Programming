from repository.repository import Repository
from service.studentService import StudentService


def testAdaugaStudentService():
    studentRepository = Repository()
    studentService = StudentService(studentRepository)
    studentService.adaugaStudent("1", "ana", "311")

    studenti = studentService.getAllStudenti()
    assert len(studenti) == 1
    assert studenti[0].getIdStudenti() == "1"

    try:
        studentService.adaugaStudent("1", "ion", "345")
        assert False
    except KeyError:
        ...

def testModificaStudentService():
    studentRepository = Repository()
    studentService = StudentService(studentRepository)
    studentService.adaugaStudent("1", "ana", "311")

    studentService.modificaStudent("1", "3", "paul")

    studenti = studentService.getAllStudenti()
    assert studenti[0].getNume() == "paul"

    try:
        studentService.modificaStudent("3", "1", "ion")
        assert False
    except KeyError:
        ...

def testStergeStudentService():
    studentRepository = Repository()
    studentService = StudentService(studentRepository)
    studentService.adaugaStudent("1", "ana" , "311")

    studentService.stergeStudent("1")

    studenti = studentService.getAllStudenti()
    assert len(studenti) == 0

    try:
        studentService.stergeStudent("1")
        assert False
    except KeyError:
        ...