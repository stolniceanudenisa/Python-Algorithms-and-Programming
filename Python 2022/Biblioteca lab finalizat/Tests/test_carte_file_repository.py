from Domain.carte import Carte
from Repository.carte_file_repository import CarteFileRepository
from utils import clear_file


def test_carte_file_repository():
    filename = 'test_carte.txt'
    clear_file(filename)
    carte_file_repository = CarteFileRepository(filename)
    carte = Carte('1', 'aa', 'bbb', 'cc')
    carte_file_repository.add(carte)
    carti = carte_file_repository.get_all()
    assert len(carti) == 1
