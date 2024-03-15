from domain.studenti import *
from repository.studenti_repo import *
from service.studenti_service import *
from ui.console import *

studentRepository = StudentiRepository("studenti.txt")
studentRepository.read()
# studentRepository.studenti[0].__str__()
# studentRepository.find_all()[0].__str__()
studentService = StudentiService(studentRepository)
console = Console(studentService)
console.Menu()
