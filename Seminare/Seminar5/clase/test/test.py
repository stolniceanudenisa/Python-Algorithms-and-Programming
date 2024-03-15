from seminar5.clase.controller.StudentController import StudentController
from seminar5.clase.repository.StudentRepository import StudentRepository
from seminar5.clase.domain.Student import Student

def test_student():
    # intitalizam un student si verificam ca metodele get_id() si get_nume() returneaza id-ul si numele lui
    student1 = Student(1, "Ana Pop")
    assert student1.get_id() == 1
    assert student1.get_nume() == "Ana Pop"
    # modificam id-ul si numele studentului, apoi verificam ca metodele get_id() si get_nume() returneaza noile valori
    student1.set_id(2)
    student1.set_nume("Ionut Popa")
    assert student1.get_id() == 2
    assert student1.get_nume() == "Ionut Popa"

def test_repository():
    repository = StudentRepository()
    lista_studenti = repository.get_all() #metoda get_all() din repository ne returneaza lista de obiecte(Studenti)
    assert len(lista_studenti) == 0 #la inceput, verificam ca lista de studenti sa fie goala
    #adaugam un student
    student1 = Student(1, "Ioan Popa")
    repository.adauga(student1)
    assert len(lista_studenti) == 1 #dupa adaugarea unui student, verificam ca lungimea listei de studenti sa devina 1

def test_controller():
    repository = StudentRepository()
    controller = StudentController(repository)
    lista_studenti = controller.get_all()
    assert len(lista_studenti) == 0 #la inceput, verificam ca lista de studenti sa fie goala
    #adaugam un student prin controller
    controller.adauga(1, "Sara Boanca")
    assert len(lista_studenti) == 1 #dupa adaugarea unui student, verificam ca lungimea listei de studenti sa devina 1

def teste():
    test_student()
    test_repository()
    test_controller()
    print("Testele au trecut!")