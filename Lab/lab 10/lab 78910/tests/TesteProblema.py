from domeniu.problema import Problema


def testProblemaLaborator():
    problemaLaborator = Problema("3_6", "descriere", "22.11.2022", )

    assert problemaLaborator.getIdProblema() == "3_6"
    assert problemaLaborator.getDescriere() == "descriere"
    assert problemaLaborator.getDeadline() == "22.11.2022"

def testProblemaLaboratorSetteri():
    problemaLaborator = Problema("3_6", "descriere", "22.11.2022", )

    problemaLaborator.setIdProblema("3_6")
    assert problemaLaborator.getIdProblema() == "3_6"

    problemaLaborator.setDescriere("description")
    assert problemaLaborator.getDescriere() == "description"

    problemaLaborator.setDeadline("31.30.2022")
    assert problemaLaborator.getDeadline() == "31.30.2022"