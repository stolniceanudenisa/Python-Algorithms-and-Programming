from seminar9.clase.controller.StudentController import StudentController
from seminar9.clase.domain.Disciplina import Disciplina
from seminar9.clase.domain.Inscriere import Inscriere
from seminar9.clase.domain.Student import Student
from seminar9.clase.repository.StudentRepository import StudentRepository
from seminar9.clase.controller.DisciplinaController import DisciplinaController
from seminar9.clase.repository.DisciplinaRepository import DisciplinaRepository
from seminar9.clase.controller.InscriereController import InscriereController
from seminar9.clase.repository.InscriereRepository import InscriereRepository
from seminar9.clase.test.test import teste
from seminar9.clase.ui.UI import UI


teste()

student_repository = StudentRepository()
disciplina_repository = DisciplinaRepository()
inscriere_repository = InscriereRepository(student_repository, disciplina_repository)

student_controller = StudentController(student_repository)
disciplina_controller = DisciplinaController(disciplina_repository)
inscriere_controller = InscriereController(inscriere_repository, student_repository, disciplina_repository)

ui = UI(student_controller, disciplina_controller, inscriere_controller)

#adaugam 3 studenti si 2 discipline predefinite si ii inscriem la ele (si le dam nota)
student1 = Student(11, "Sara")
student2 = Student(12, "Dana")
student3 = Student(13, "Andrei")
student_repository.adauga(student1)
student_repository.adauga(student2)
student_repository.adauga(student3)

disciplina1 = Disciplina(101, "AP-22", "Radu Gaceanu")
disciplina2 = Disciplina(102, "Algebra", "Septimiu Crivei")
disciplina_repository.adauga(disciplina1)
disciplina_repository.adauga(disciplina2)

inscriere1 = Inscriere(1,11,101,10)#am inscris-o pe Sara la AP-22 si i-am dat nota 8
inscriere2 = Inscriere(2,11,102,9)#am inscris-o pe Sara la Algebra si i-am dat nota 9
inscriere3 = Inscriere(3,12,101,9)#am inscris-o pe Dana la AP-22 si i-am dat nota 10
inscriere4 = Inscriere(4,12,102,8)#am inscris-o pe Dana la Algebra si i-am dat nota 8
inscriere5 = Inscriere(5,13,101,9)#l-am inscris pe Andrei la AP-22 si i-am dat nota 10
inscriere6 = Inscriere(6,13,102,9)#l-am inscris pe Andrei la Algebra si i-am dat nota 9
inscriere_repository.adauga(inscriere1)
inscriere_repository.adauga(inscriere2)
inscriere_repository.adauga(inscriere3)
inscriere_repository.adauga(inscriere4)
inscriere_repository.adauga(inscriere5)
inscriere_repository.adauga(inscriere6)

#rulam programul nostru
ui.program()