from domain.Locatie import Locatie
from domain.LocationValidator import LocationValidator
from repository.comanda_repository import OrderRepository
from repository.locatie_repository import LocatieRepository
from service.service_exception import ServiceException


class LocationService:
    '''
    '''

    def __init__(self, location_repo: LocatieRepository, location_validator: LocationValidator, order_repo: OrderRepository):
        '''
        '''
        self.__repository = location_repo
        self.__validator = location_validator
        self.__order_repository = order_repo
        self.__undo_operations = []

    def add_location(self, id, strada, numar, bloc, scara, indicatii):
        '''

        '''
        location = Locatie(id,strada, numar, bloc, scara, indicatii)
        self.__validator.validate(location)
        self.__repository.create(location)
        self.__undo_operations.append(lambda: self.__repository.delete(location.id))


    def delete_location(self, id):
        if len(self.__order_repository.findByLocationId(id)) > 0:
            raise ServiceException('Locatia nu poate fi stearsa')
        location_to_delete = self.__repository.read(id)
        if location_to_delete is not None:
            self.__repository.delete(id)
            self.__undo_operations.append(lambda: self.__repository.create(location_to_delete))


    def get_all(self) -> [Locatie]:
        return self.__repository.read()


    def sort_streets(self):
        streets = self.get_all()
        return sorted(streets, key=lambda x: len(x.indicatii), reverse=True)

    def undo(self):
        if len(self.__undo_operations) > 0:
            undo_op = self.__undo_operations.pop()
            undo_op()