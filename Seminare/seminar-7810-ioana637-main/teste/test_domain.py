from domain.Car import Car
from domain.Locatie import Locatie


def test_locatie():
    locatie = Locatie(13, 'strada', 18, 'bloc a4', 'I', 'indicatii')
    assert locatie.strada == 'strada'
    # TODO

def test_comanda():
    pass
#     TODO

def test_car():
    car = Car(1, 13, 'standard', True, 'skoda')
    assert car.indicativ == 13
    assert car.confort == 'standard'
    assert car.plata_card == True
    assert car.model == 'skoda'
    car.indicativ = 34
    car.confort = 'high'
    car.plata_card = False
    car.model = 'model2'
    assert car.indicativ == 34
    assert car.confort == 'high'
    assert car.plata_card == False
    assert car.model == 'model2'


def test_domain():
    test_car()
    test_locatie()
    test_comanda()