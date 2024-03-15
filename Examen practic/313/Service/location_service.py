from typing import List

from Domain.location import Location
from Repository.location_repository import LocationRepository


class LocationService:
    def __init__(self,
                 location_repository: LocationRepository):
        self.location_repository = location_repository

    def add(self,
            id_location: str,
            street_name: str,
            street_num: int,
            block: str,
            entry: str,
            other_info: str):
        location = Location(id_location, street_name,
                            street_num, block,
                            entry, other_info)
        self.location_repository.create(location)

    def update(self,
               id_location: str,
               street_name: str,
               street_num: int,
               block: str,
               entry: str,
               other_info: str):
        location = Location(id_location, street_name,
                            street_num, block,
                            entry, other_info)
        self.location_repository.update(location)

    def delete(self, id_location: str):
        self.location_repository.delete(id_location)

    def get_all(self) -> List[Location]:
        return self.location_repository.read()
