from seminar6.clase.controller.StudentController import StudentController
from seminar6.clase.repository.StudentRepository import StudentRepository
from seminar6.clase.controller.DisciplinaController import DisciplinaController
from seminar6.clase.repository.DisciplinaRepository import DisciplinaRepository
from seminar6.clase.test.test import teste
from seminar6.clase.ui.UI import UI

teste()

student_repository = StudentRepository()
disciplina_repository = DisciplinaRepository()

student_controller = StudentController(student_repository)
disciplina_controller = DisciplinaController(disciplina_repository)

ui = UI(student_controller, disciplina_controller)

ui.program()