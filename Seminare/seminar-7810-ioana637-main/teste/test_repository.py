from domain.Car import Car
from domain.Comanda import Comanda
from domain.Locatie import Locatie
from repository.car_file_repository import CarFileRepository
from repository.car_repository import CarRepository
from repository.comanda_repository import OrderRepository
from repository.locatie_repository import LocatieRepository


def test_car_file_repository():
    # Cand se testeaza un file repository, un repository care stocheaza datele intr-un fisier text
    # Se recomanda folosirea unui fisier de test, altul decat cel care se foloseste cand se ruleaza aplicatia main

    repo = CarFileRepository('test_cars.pkl')
    repo.create(Car(1, 13, 'standard', True, 'skoda'))
    assert len(repo.read()) == 1
    repo.update(Car(1, 13, 'high', False, 'logan'))
    assert repo.read(1).confort == 'high'
    repo.delete(1)
    assert len(repo.read()) == 0

def test_car_repository():
    repo = CarRepository()
    repo.create(Car(1, 13, 'standard', True, 'skoda'))
    assert len(repo.read()) == 1
    repo.update(Car(1, 13, 'high', False, 'logan'))
    assert repo.read(1).confort == 'high'
    repo.delete(1)
    assert len(repo.read()) == 0


def test_order_repository():
    repo = OrderRepository()
    # id, car_id, locatie_id, time, cost_km, distance, status
    repo.create(Comanda(1, 13, 23, 34, 45, 100, 'status'))
    assert len(repo.read()) == 1
    repo.update(Comanda(1, 13, 23, 34, 45, 100, 'status'))
    assert repo.read(1).time == 34
    repo.delete(1)
    assert len(repo.read()) == 0

def test_locatie_repository():
    repo = LocatieRepository()
    repo.create(Locatie(1, 'strada',12, 'bloc', 'scara', 'obs'))
    assert len(repo.read()) == 1
    repo.update(Locatie(1, 'strada2',12, 'bloc', 'scara', 'obs'))
    assert repo.read(1).strada == 'strada2'
    repo.delete(1)
    assert len(repo.read()) == 0

    try:
        repo.delete(23)
        assert False
    except Exception:
        assert True


def test_all_repository():
    test_order_repository()
    test_car_repository()
    test_car_file_repository()
    test_locatie_repository()
