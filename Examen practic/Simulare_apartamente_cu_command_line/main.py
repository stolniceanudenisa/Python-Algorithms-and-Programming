from Repo.apartament_repo import ApartamentFileRepo
from Service.apartament_service import ApartamentService
from Tests.teste import Teste
from UI.console import Console


def main():
    apartament_repo=ApartamentFileRepo("apartamente.txt")
    apartament_service=ApartamentService(apartament_repo)
    console=Console(apartament_repo,apartament_service)
    console.run_ui()



if __name__ == '__main__':
    Teste()
    main()