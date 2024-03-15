from Domain.car import Car
from Repository.car_repository import CarRepository
from utils import clear_file


def test_car_repository():
    filename = 'test_car_repo.json'
    clear_file(filename)
    car_repository = CarRepository(filename)
    assert car_repository.read() == []

    added = Car('1', 'fda23', 'standard', True, 'Logan')
    car_repository.create(added)
    assert car_repository.read('1') == added

    # TODO