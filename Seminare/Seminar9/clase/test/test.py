from seminar10.clase.controller.InscriereController import InscriereController
from seminar10.clase.controller.StudentController import StudentController
from seminar10.clase.domain.ValidatorException import ValidatorException
from seminar10.clase.domain.DisciplinaValidator import DisciplinaValidator
from seminar10.clase.repository.DisciplinaFileRepository import DisciplinaFileRepository
from seminar10.clase.repository.InscriereFileRepository import InscriereFileRepository
from seminar10.clase.repository.InscriereRepository import InscriereRepository
from seminar10.clase.repository.StudentFileRepository import StudentFileRepository
from seminar10.clase.repository.StudentRepository import StudentRepository
from seminar10.clase.controller.DisciplinaController import DisciplinaController
from seminar10.clase.repository.DisciplinaRepository import DisciplinaRepository, InexistentIDException, \
    DuplicateIDException
from seminar10.clase.domain.Student import Student
from seminar10.clase.domain.Disciplina import Disciplina
from seminar10.clase.domain.Inscriere import Inscriere

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
    disciplina_validator = DisciplinaValidator()
    assert disciplina_validator.valideaza(disciplina1) == True

    #testam o validare cand se arunca eroare
    disciplina1.set_nume("A")
    try:
        disciplina_validator.valideaza_nume(disciplina1.get_nume())
        assert False
    except ValidatorException:
        assert True


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

    #incercam sa adaugam un student cu acelasi id, ca sa testam cazul de eroare DuplicateIDException
    try:
        repository.adauga(student1)
        assert False
    except DuplicateIDException:
        assert True

def test_student_file_repository():
    '''
    Cand testati in file repository, asigurati-va ca fisierul este initial gol.
    Faceti testele de care aveti nevoie, apoi la final stergeti entitatile adaugate, ca sa nu apara erori data urmatoare cand rulati programul
    '''
    repository = StudentFileRepository("test/studenti_test.txt")
    lista_studenti = repository.get_all()  # metoda get_all() din repository ne returneaza lista de obiecte(Studenti)
    assert len(lista_studenti) == 0  # la inceput, verificam ca lista de studenti sa fie goala
    # adaugam un student
    student1 = Student(1, "Ioan Popa")
    repository.adauga(student1)
    assert len(lista_studenti) == 1  # dupa adaugarea unui student, verificam ca lungimea listei de studenti sa devina 1

    # incercam sa adaugam un student cu acelasi id, ca sa testam cazul de eroare DuplicateIDException
    try:
        repository.adauga(student1)
        assert False
    except DuplicateIDException:
        assert True

    repository.sterge(1) #e important sa stergem studentul adaugat in fisier, pentru ca daca rulam de mai multe ori testele, starea fisierului la inceput sa fie tot goala
    assert len(lista_studenti) == 0

def test_disciplina_repository():
    repository = DisciplinaRepository()
    lista_discipline = repository.get_all()
    assert len(lista_discipline) == 0
    disciplina1 = Disciplina(1, "AP-22", "Sara")
    repository.adauga(disciplina1)
    assert len(lista_discipline) == 1
    disciplina_noua = Disciplina(1, "Algoritmi si programare", "Sara")
    repository.modifica(disciplina_noua)
    assert len(lista_discipline) == 1 #in urma modificarii lungimea listei nu se schimba
    assert repository.gaseste_dupa_id(1) == 0 #disciplina cu id=1 se afla pe pozitia 0 in lista din repository
    assert repository.gaseste_dupa_id(2) == -1 #disciplina cu id=2 nu exista in repository

    #testam cazul in care adaugam o disciplina cu acelasi ID
    try:
        repository.adauga(disciplina_noua)
        assert False
    except DuplicateIDException:
        assert True

    repository.sterge(1)
    assert len(lista_discipline) == 0
    assert repository.gaseste_dupa_id(1) == -1 #dupa stergere, disciplina cu id=1 nu se mai gaseste in repository

    # testam cazul in care vrem sa stergem o disciplina care nu exista (nu o gasim dupa ID)
    try:
        repository.sterge(345)
        assert False
    except InexistentIDException:
        assert True

    #testam cazul in care vrem sa modificam o disciplina care nu exista (nu o gasim dupa ID)
    disciplina_al_carei_id_nu_exista = Disciplina(345, "Disciplina inexistenta", "Profesor inexistent")
    try:
        repository.modifica(disciplina_al_carei_id_nu_exista)
        assert False
    except InexistentIDException:
        assert True

def test_disciplina_file_repository():
    repository = DisciplinaFileRepository("test/discipline_test.txt")
    lista_discipline = repository.get_all()
    assert len(lista_discipline) == 0
    disciplina1 = Disciplina(1, "AP-22", "Sara")
    repository.adauga(disciplina1)
    assert len(lista_discipline) == 1
    disciplina_noua = Disciplina(1, "Algoritmi si programare", "Sara")
    repository.modifica(disciplina_noua)
    assert len(lista_discipline) == 1  # in urma modificarii lungimea listei nu se schimba
    assert repository.gaseste_dupa_id(1) == 0  # disciplina cu id=1 se afla pe pozitia 0 in lista din repository
    assert repository.gaseste_dupa_id(2) == -1  # disciplina cu id=2 nu exista in repository

    # testam cazul in care adaugam o disciplina cu acelasi ID
    try:
        repository.adauga(disciplina_noua)
        assert False
    except DuplicateIDException:
        assert True

    repository.sterge(1) #e important sa stergem disciplina adaugata in fisier, pentru ca daca rulam de mai multe ori testele, starea fisierului la inceput sa fie tot goala
    assert len(lista_discipline) == 0

    assert repository.gaseste_dupa_id(1) == -1  # dupa stergere, disciplina cu id=1 nu se mai gaseste in repository

    # testam cazul in care vrem sa stergem o disciplina care nu exista (nu o gasim dupa ID)
    try:
        repository.sterge(345)
        assert False
    except InexistentIDException:
        assert True

    # testam cazul in care vrem sa modificam o disciplina care nu exista (nu o gasim dupa ID)
    disciplina_al_carei_id_nu_exista = Disciplina(345, "Disciplina inexistenta", "Profesor inexistent")
    try:
        repository.modifica(disciplina_al_carei_id_nu_exista)
        assert False
    except InexistentIDException:
        assert True

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

    #asa testam metode care arunca erori
    try:
        inscriere_repository.adauga(inscriere1)
        assert False
    except KeyError:
        assert True

    #e important sa stergem ce am adaugat in fisier, pentru ca daca rulam de mai multe ori testele, starea fisierului la inceput sa fie tot goala
    inscriere_repository.sterge(1)
    assert len(lista_inscrieri) == 0

    student_repository.sterge(1)
    disciplina_repository.sterge(1)

def test_inscriere_file_repository():
    student_file_repository = StudentFileRepository("test/studenti_test.txt")
    disciplina_file_repository = DisciplinaFileRepository("test/discipline_test.txt")
    inscriere_file_repository = InscriereFileRepository("test/inscrieri_test.txt", student_file_repository, disciplina_file_repository)
    student1 = Student(1, "Andrei")
    disciplina1 = Disciplina(1, "AP-22", "Sara")
    student_file_repository.adauga(student1)
    disciplina_file_repository.adauga(disciplina1)
    inscriere1 = Inscriere(1, 1, 1, 10)
    lista_inscrieri = inscriere_file_repository.get_all()
    assert len(lista_inscrieri) == 0
    inscriere_file_repository.adauga(inscriere1)
    assert len(lista_inscrieri) == 1
    inscriere_file_repository.sterge(1)
    disciplina_file_repository.sterge(1)
    student_file_repository.sterge(1)

def test_student_controller():
    repository = StudentRepository()
    controller = StudentController(repository)
    lista_studenti = controller.get_all()
    assert len(lista_studenti) == 0 #la inceput, verificam ca lista de studenti sa fie goala
    #adaugam un student prin controller
    controller.adauga(1, "Sara Boanca")
    assert len(lista_studenti) == 1 #dupa adaugarea unui student, verificam ca lungimea listei de studenti sa devina 1

    try:
        controller.adauga(1, "Student pe care nu il putem adauga pentru ca are acelasi ID")
        assert False
    except DuplicateIDException:
        assert True

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
    #incercam sa modificam o disciplina care nu exista
    try:
        controller.modifica(1, "Algoritmi si programare", "Sara")
        assert False
    except InexistentIDException:
        assert True

    #incercam sa stergem o disciplina care nu exista
    try:
        controller.sterge(123)
        assert False
    except InexistentIDException:
        assert True

def test_inscriere_controller():
    student_repository = StudentRepository()
    disciplina_repository = DisciplinaRepository()
    inscriere_repository = InscriereRepository(student_repository, disciplina_repository)
    inscriere_controller = InscriereController(inscriere_repository, student_repository, disciplina_repository)
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
    test_student_file_repository()
    test_disciplina_repository()
    test_disciplina_file_repository()
    test_inscriere_repository()
    test_inscriere_file_repository()
    test_student_controller()
    test_disciplina_controller()
    print("Testele au trecut!!")