from domeniu.student import Student


def testStudent():
    student = Student("1", "ana", "311", "")

    assert student.getIdStudent() == "1"
    assert student.getNume() == "ana"
    assert student.getGrup() == "311"
    assert student.getIdProblemaLaborator() == ""

def testStudentSetteri():
    student = Student("1", "ana", "311" , "")

    student.setIdStudent("3")
    assert student.getIdStudent() == "3"

    student.setNume("paul")
    assert student.getNume() == "paul"

    student.setGrup("999")
    assert student.getGrup() == "999"

    student.setProblemaLaborator("")
    assert student.getIdProblemaLaborator() == ""
