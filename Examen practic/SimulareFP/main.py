import unittest

from Business.Service import Service
from Prezentare.UI import Consola
from Repository.RepositoryAnimal import RepositoryAnimal
from Repository.RepositoryAnimalFile import RepositoryAnimalFile
from Testare.Teste import Teste
if __name__=='__main__':
    unittest.main(exit=False)
    print("1.Ruleaza cu fisiere\n2.Ruleaza cu memorie")
    cmd=int(input(">>>"))
    if cmd==1:
        repo=RepositoryAnimalFile('hotel_animale.txt')
        service=Service(repo)
        consola=Consola(service)
        consola.runUI()
    else:
        if cmd==2:
            repo=RepositoryAnimal()
            service = Service(repo)
            consola = Consola(service)
            consola.runUI()

