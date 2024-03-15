from teste.testAngajat import testAngajat, testAngajatSetteri
from teste.testAngajatRepository import testAdaugaAngajatRepository, testModificaAngajatRepository, \
    testStergeAngajatRepository
from teste.testAngajatService import testAdaugaAngajatService, testModificaAngajatService, testStergeAngajatService


def testAll():
    testAngajat()
    testAngajatSetteri()

    testAdaugaAngajatRepository()
    testModificaAngajatRepository()
    testStergeAngajatRepository()

    testAdaugaAngajatService()
    testModificaAngajatService()
    testStergeAngajatService()