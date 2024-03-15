from seminar5.clase.controller.StudentController import StudentController
from seminar5.clase.repository.StudentRepository import StudentRepository
from seminar5.clase.test.test import teste
from seminar5.clase.ui.UI import UI

teste()
repository = StudentRepository()
controller = StudentController(repository)
ui = UI(controller)
ui.program()