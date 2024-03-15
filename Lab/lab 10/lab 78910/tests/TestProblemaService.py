from repository.repositoryInMemory import Repository
from service.problemaService import ProblemaLaboratorService


def testAdaugaProblemaLaboratorService():
    problemaLaboratorRepository = Repository()
    problemaLaboratorService = ProblemaLaboratorService(problemaLaboratorRepository)
    problemaLaboratorService.adaugaProblemaLaborator("3_7", "descriere", "22.11.2022")

    problemeLaborator = problemaLaboratorService.getAllProblemeLaborator()
    assert len(problemeLaborator) == 1
    assert problemeLaborator[0].getIdStudenti() == "3_7"

    try:
        problemaLaboratorService.adaugaProblemaLaborator("3_8", "descriere1", "14.24.2022")
        assert False
    except KeyError:
        ...

def testModificaProblemaLaboratorService():
    problemaLaboratorRepository = Repository()
    problemaLaboratorService = ProblemaLaboratorService(problemaLaboratorRepository)
    problemaLaboratorService.adaugaProblemaLaborator("3_7", "descriere", "22.11.2022")

    problemaLaboratorService.modificaProblemaLaborator("3_7", "descriere_noua", "22.12.2022")

    problemeLaborator = problemaLaboratorService.getAllProblemeLaborator()
    assert problemeLaborator[0].getDescriere() == "descriere"

    try:
        problemaLaboratorService.modificaProblemaLaborator("3_8", "descriere_noua2", "21.10.2022")
        assert False
    except KeyError:
        ...

def testStergeProblemaLaboratorService():
    problemaLaboratorRepository = Repository()
    problemaLaboratorService = ProblemaLaboratorService(problemaLaboratorRepository)
    problemaLaboratorService.adaugaProblemaLaborator("3_2", "descriere" , "11.10.2022")

    problemaLaboratorService.stergeProblemaLaborator("3_2")

    problemeLaborator = problemaLaboratorService.getAllProblemeLaborator()
    assert len(problemeLaborator) == 0

    try:
        problemaLaboratorService.stergeProblemaLaborator("3_2")
        assert False
    except KeyError:
        ...