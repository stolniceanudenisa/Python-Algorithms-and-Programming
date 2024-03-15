from Repo.imobil_file_repo import ImobilFileRepo
from Service.imobil_service import ImobilService
from UI.console import Console


def main():
    imobil_repo = ImobilFileRepo("imobil.txt")
    imobil_service = ImobilService(imobil_repo)
    console = Console(imobil_repo, imobil_service)
    console.run_console()


if __name__ == '__main__':
    # test_all()
    main()
