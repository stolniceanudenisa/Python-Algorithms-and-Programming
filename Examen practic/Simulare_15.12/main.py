from Repo.clasament_repo import ClasamentFileRepo
from Repo.concurent_repo import ConcurentFileRepo
from Service.clasament_service import ClasamentService
from Service.concurent_service import ConcurentService
from Tests.Teste_clasament import TesteClasament
from Tests.Teste_concurenti import TesteConcurent
from UI.console import Console


def main():
    concurent_repo=ConcurentFileRepo("lista_concurenti.txt")
    concurent_service=ConcurentService(concurent_repo)
    clasament_repo = ClasamentFileRepo("lista_castigatori.txt")
    clasament_service = ClasamentService(clasament_repo)
    console=Console(concurent_repo,concurent_service,clasament_repo,clasament_service)
    console.run_ui()


if __name__ == '__main__':
    TesteConcurent()
    TesteClasament()
    main()
