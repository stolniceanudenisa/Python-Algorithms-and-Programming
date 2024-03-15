from Tests.testAngajatRepository import testadd_ang_repository, testmodifica_ang_repository, teststerge_ang_repository
from Tests.testAngajatService import testadaugaAngajat_service, testmodificaAngajat_service, teststergeAngajat_service
from Tests.testAngajati import testAngajatGetteri, testAngajatSetteri


def testAll():
    testAngajatGetteri()
    testAngajatSetteri()

    testadd_ang_repository()
    testmodifica_ang_repository()
    teststerge_ang_repository()

    testadaugaAngajat_service()
    testmodificaAngajat_service()
    teststergeAngajat_service()
