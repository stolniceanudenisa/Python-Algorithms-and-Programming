from typing import List

from Domain.add_operation import AddOperation
from Domain.location import Location
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService
from ViewModels.street_and_len import StreetAndLen


class LocationService:
    def __init__(self,
                 location_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.location_repository = location_repository
        self.undo_redo_service = undo_redo_service

    def add_location(self,
                     id_location: str,
                     street_name: str,
                     street_number: int):
        """
        TODO
        """
        location = Location(id_location, street_name, street_number)
        self.location_repository.create(location)

        self.undo_redo_service.clear_redo()
        add_operation = AddOperation(self.location_repository, location)
        self.undo_redo_service.add_to_undo(add_operation)

    def update_location(self,
                        id_location: str,
                        street_name: str,
                        street_number: int):
        """
        TODO
        """
        location = Location(id_location, street_name, street_number)
        self.location_repository.update(location)

    def delete_location(self, id_location: str):
        self.location_repository.delete(id_location)

    def get_all(self) -> List[Location]:
        return self.location_repository.read()

    def get_ordered_by_street_len_desc(self) -> List[StreetAndLen]:
        """
        :return: strazile ordonate descrescator dupa lungimea numelui.
        """

        def inner(locations):
            if not locations:
                return []

            loc = locations[0]
            return [StreetAndLen(loc.street_name, len(loc.street_name))] + inner(locations[1:])

        # [1,2,3] + [5, 7, 4] == [1, 2, 3, 5, 7, 4] (concatenare de liste)

        locations = self.get_all()
        streets_and_lens = inner(locations)

        # locations = self.get_all()
        # #streets_and_lens = map(lambda loc: StreetAndLen(loc.street_name, len(loc.street_name)), locations)
        # streets_and_lens = [StreetAndLen(loc.street_name, len(loc.street_name)) for loc in locations]
        return sorted(streets_and_lens, key=lambda x: x.street_name_len, reverse=True)
