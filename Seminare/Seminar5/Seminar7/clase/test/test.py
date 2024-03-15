from seminar7.clase.controller.InscriereController import InscriereController
from seminar7.clase.controller.StudentController import StudentController
from seminar7.clase.repository.InscriereRepository import InscriereRepository
from seminar7.clase.repository.StudentRepository import StudentRepository
from seminar7.clase.controller.DisciplinaController import DisciplinaController
from seminar7.clase.repository.DisciplinaRepository import DisciplinaRepository
from seminar7.clase.domain.Student import Student
from seminar7.clase.domain.Disciplina import Disciplina
from seminar7.clase.domain.Inscriere import Inscriere

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

def test_disciplina():
    disciplina1 = Disciplina(1, "AP-22", "Sara")
    assert disciplina1.get_id() == 1
    assert disciplina1.get_nume() == "AP-22"
    assert disciplina1.get_profesor() == "Sara"
    disciplina1.set_id(2)
    disciplina1.set_nume("Algoritmi si programare")
    disciplina1.set_profesor("Sara Boanca")
    assert disciplina1.get_id() == 2
    assert disciplina1.get_nume() == "Algoritmi si programare"
    assert disciplina1.get_profesor() == "Sara Boanca"

def test_inscriere():
    inscriere1 = Inscriere(1, 1, 1, 5)
    assert inscriere1.get_id() == 1
    assert inscriere1.get_student_id() == 1
    assert inscriere1.get_disciplina_id() == 1
    assert inscriere1.get_nota() == 5
    inscriere1.set_id(2)
    inscriere1.set_student_id(2)
    inscriere1.set_disciplina_id(2)
    inscriere1.set_nota(10)
    assert inscriere1.get_id() == 2
    assert inscriere1.get_student_id() == 2
    assert inscriere1.get_disciplina_id() == 2
    assert inscriere1.get_nota() == 10

def test_student_repository():
    repository = StudentRepository()
    lista_studenti = repository.get_all() #metoda get_all() din repository ne returneaza lista de obiecte(Studenti)
    assert len(lista_studenti) == 0 #la inceput, verificam ca lista de studenti sa fie goala
    #adaugam un student
    student1 = Student(1, "Ioan Popa")
    repository.adauga(student1)
    assert len(lista_studenti) == 1 #dupa adaugarea unui student, verificam ca lungimea listei de studenti sa devina 1

def test_disciplina_repository():
    repository = DisciplinaRepository()
    lista_discipline = repository.get_all()
    assert len(lista_discipline) == 0
    disciplina1 = Disciplina(1, "AP-22", "Sara")
    repository.adauga(disciplina1)
    assert len(lista_discipline) == 1
    repository.modifica(1, "Algoritmi si programare", "Sara")
    assert len(lista_discipline) == 1 #in urma modificarii lungimea listei nu se schimba
    assert repository.gaseste_disciplina_dupa_id(1) == 0 #disciplina cu id=1 se afla pe pozitia 0 in lista din repository
    assert repository.gaseste_disciplina_dupa_id(2) == -1 #disciplina cu id=2 nu exista in repository
    repository.sterge(1)
    assert len(lista_discipline) == 0
    assert repository.gaseste_disciplina_dupa_id(1) == -1 #dupa stergere, disciplina cu id=1 nu se mai gaseste in repository

def test_inscriere_repository():
    student_repository = StudentRepository()
    disciplina_repository = DisciplinaRepository()
    inscriere_repository = InscriereRepository(student_repository, disciplina_repository)
    student1 = Student(1,"Andrei")
    disciplina1 = Disciplina(1,"AP-22","Sara")
    student_repository.adauga(student1)
    disciplina_repository.adauga(disciplina1)
    inscriere1 = Inscriere(1,1,1,10)
    lista_inscrieri = inscriere_repository.get_all()
    assert len(lista_inscrieri) == 0
    inscriere_repository.adauga(inscriere1)
    assert len(lista_inscrieri) == 1

def test_student_controller():
    repository = StudentRepository()
    controller = StudentController(repository)
    lista_studenti = controller.get_all()
    assert len(lista_studenti) == 0 #la inceput, verificam ca lista de studenti sa fie goala
    #adaugam un student prin controller
    controller.adauga(1, "Sara Boanca")
    assert len(lista_studenti) == 1 #dupa adaugarea unui student, verificam ca lungimea listei de studenti sa devina 1

def test_disciplina_controller():
    repository = DisciplinaRepository()
    controller = DisciplinaController(repository)
    lista_discipline = controller.get_all()
    assert len(lista_discipline) == 0
    controller.adauga(1, "AP-22", "Sara")
    assert len(lista_discipline) == 1
    controller.modifica(1, "Algoritmi si programare", "Sara")
    assert len(lista_discipline) == 1 #in urma modificarii lungimea listei nu se schimba
    controller.sterge(1)
    assert len(lista_discipline) == 0

def test_inscriere_controller():
    student_repository = StudentRepository()
    disciplina_repository = DisciplinaRepository()
    inscriere_repository = InscriereRepository(student_repository, disciplina_repository)
    inscriere_controller = InscriereController(inscriere_repository)
    lista_inscrieri = inscriere_controller.get_all()
    assert len(lista_inscrieri) == 0
    student1 = Student(1, "Andrei")
    disciplina1 = Disciplina(1, "AP-22", "Sara")
    student_repository.adauga(student1)
    disciplina_repository.adauga(disciplina1)
    inscriere_controller.adauga(1,1,1,10)
    assert len(lista_inscrieri) == 1

def teste():
    test_student()
    test_disciplina()
    test_inscriere()
    test_student_repository()
    test_disciplina_repository()
    test_inscriere_repository()
    test_student_controller()
    test_disciplina_controller()
    print("Testele au trecut!!!")