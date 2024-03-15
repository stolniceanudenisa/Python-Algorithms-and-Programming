from Domain.gradevalidator import gradeValidator
from Domain.sessionvalidator import SessionValidator
from Repository.json_repository import JsonRepository
from Service.gradeservice import gradeService
from Service.sessionservice import sessionService
from UserInterface.UI import Console


def main():
    graderepository = JsonRepository("grades.json")
    gradevalidator = gradeValidator()
    gradeservice = gradeService(graderepository, gradevalidator)

    sessionrepository = JsonRepository("sessions.json")
    sessionvalidator = SessionValidator()
    sessionservice = sessionService(sessionrepository, sessionvalidator,
                                    graderepository)
    console = Console(sessionservice, gradeservice)
    console.runConsole()


if __name__ == "__main__":
    main()