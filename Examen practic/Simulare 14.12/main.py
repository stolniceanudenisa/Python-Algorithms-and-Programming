from Infrastructure.repo_animal import RepoAnimal
from Bussines.service_animal import ServiceAnimal
from Interfata.ui import Ui
from Teste.teste_animal import Teste

if __name__ == '__main__':

    file_path = "animale.txt"
    repo_animale = RepoAnimal(file_path)
    service_animale = ServiceAnimal(repo_animale)

    repo_animale_teste = RepoAnimal(file_path)
    service_animale_teste = ServiceAnimal(repo_animale_teste)
    teste = Teste(service_animale_teste, repo_animale_teste)
    teste.run_all()

    ui = Ui(service_animale)
    ui.meniu()
    ui.run()
