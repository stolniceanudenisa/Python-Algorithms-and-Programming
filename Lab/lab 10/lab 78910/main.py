from repository.repositoryJson import RepositoryJson
from service.studentService import StudentService
from ui.consola import Consola
from service.problemaService import ProblemaLaboratorService
from service.asignareService import AsignareService
from tests.testAll import testAll

def main():
    # testAll()

    studentRepository = RepositoryJson("./studenti.json")
    problemaLaboratorRepository = RepositoryJson("./problema_laborator.json")
    asignareRepository = RepositoryJson("./asignare.json")

    studentService = StudentService(studentRepository, asignareRepository)
    problemaLaboratorService = ProblemaLaboratorService(problemaLaboratorRepository, asignareRepository)
    asignareService = AsignareService(asignareRepository, studentRepository, problemaLaboratorRepository)

    studentRepository.loadFromFile()
    problemaLaboratorRepository.loadFromFile()
    asignareRepository.loadFromFile()

    consola = Consola(studentService, problemaLaboratorService, asignareService)
    consola.meniu()


main()
