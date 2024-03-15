from UserInterface.ConsoleUI import ConsoleMenu
from UserInterface.GUI import GUI
from Controllers.service import ServiceBooks,ServiceClients,ServiceRentals,ServiceStatistics,ServiceUndoRedo
from Domain.entities import Settings
from Domain.validation import BookValidator,ClientValidator,RentalValidator
from Repository.repo import Repo,FileRepo,RepoUndoRedo,EntriesGenerator,JSONFileRepo

if __name__=="__main__":

    settings = Settings("settings.properties")
    Books_Repository, Clients_Repository, Rentals_Repository = settings.getRepos(Repo,FileRepo,JSONFileRepo)
    UndoRedo_Repo = RepoUndoRedo()
    generateEntries = settings.getEntries(EntriesGenerator)

    BookContr = ServiceBooks(Books_Repository,BookValidator(),UndoRedo_Repo,generateEntries)
    ClientContr = ServiceClients(Clients_Repository,ClientValidator(),UndoRedo_Repo,generateEntries)
    RentalContr = ServiceRentals(Rentals_Repository,RentalValidator(),Books_Repository,Clients_Repository,UndoRedo_Repo,generateEntries)
    StatisticsContr = ServiceStatistics(Books_Repository,Clients_Repository,Rentals_Repository)
    UndoRedoContr = ServiceUndoRedo(Books_Repository,Clients_Repository,Rentals_Repository,UndoRedo_Repo)

    app_UI = settings.getUI(ConsoleMenu,GUI)(BookContr,ClientContr,RentalContr,StatisticsContr,UndoRedoContr)
    """
        Program start point
    """
    app_UI.run()