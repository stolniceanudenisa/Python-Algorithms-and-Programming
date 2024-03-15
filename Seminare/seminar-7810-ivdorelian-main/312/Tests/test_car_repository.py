from Domain.car import Car
from Repository.json_repository import JsonRepository
from utils import clear_file


def test_car_repository():
    filename = 'test_cars.json'
    clear_file(filename)
    car_repository = JsonRepository(filename)
    added = Car('1', '32s', 'standard', 'fdfs')
    car_repository.create(added)
    assert car_repository.read(added.id_entity) == added
