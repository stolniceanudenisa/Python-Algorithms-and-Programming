from Repository.costum_repo import CostumFileRepo
from Service.costum_service import CostumService
from Teste.test_domain import Test_domain
from Teste.test_repo import Test_repo
from Teste.test_service import Test_service
from UI.console import Console


def main():
    costum_repo=CostumFileRepo("costum.txt")
    costum_service=CostumService(costum_repo)

    console=Console(costum_repo,costum_service)
    console.run_ui()



if __name__ == '__main__':
    Test_domain()
    Test_repo()
    Test_service()
    main()



