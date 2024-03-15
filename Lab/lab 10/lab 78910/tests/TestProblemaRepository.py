from domeniu.problema import Problema
from repository.problemaLaboratorRepository import ProblemaLaboratorRepository


def testAdaugaProblemaLaboratorRepository():
    problemaLaboratorRepository = ProblemaLaboratorRepository()
    problemaLaborator = Problema("3_7", "descriere", "31.20.2022")

    problemaLaboratorRepository.adauga(problemaLaborator)

    problemaLaboratori = problemaLaboratorRepository.getAll()
    assert len(problemaLaboratori) == 1
    assert problemaLaboratori[0].getIdProblemaLaborator() == "3_7"

    try:
        problemaLaboratorRepository.adauga(problemaLaborator)
        assert False
    except KeyError:
        ...

def testModificaProblemaLaboratorRepository():
    problemaLaboratorRepository = ProblemaLaboratorRepository()
    problemaLaborator = Problema("3_7", "descriere1", "24.10.2020")
    problemaLaboratorNou1 = Problema("3_7", "descriere2", "24.10.2021")
    problemaLaboratorNou2 = Problema("4_7", "descriere3", "25.11.2022")
    problemaLaboratorRepository.adauga(problemaLaborator)

    problemaLaboratorRepository.modifica(problemaLaborator.getIdProblema(), problemaLaboratorNou1)

    problemaLaborator = problemaLaboratorRepository.getAll()
    assert problemaLaborator[0].getDescriere() == "descriere1"

    try:
        problemaLaboratorRepository.modifica(problemaLaborator.getIdProblemaLaborator(), problemaLaboratorNou2)
        assert False
    except KeyError:
        ...

def testStergeProblemaLaboratorRepository():
    problemaLaboratorRepository = ProblemaLaboratorRepository()
    problemaLaborator = Problema("3_7", "descriere", "22.11.2022")
    problemaLaboratorRepository.adauga(problemaLaborator)

    problemaLaboratorRepository.sterge("3_7")

    assert len(problemaLaboratorRepository.getAll()) == 0

    try:
        problemaLaboratorRepository.sterge("!")
        assert False
    except KeyError:
        ...