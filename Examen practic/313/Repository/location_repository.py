from typing import Dict, Union, Optional, List

import jsonpickle

from Domain.location import Location


class LocationRepository:

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __read_file(self):
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[str, Location]):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(objects))

    def create(self, location: Location) -> None:
        """
        TODO
        :param location:
        :return:
        """
        locations = self.__read_file()
        if self.read(location.id_location) is not None:
            raise KeyError(f'Exista deja o locatie id-ul {location.id_location}.')

        locations[location.id_location] = location
        self.__write_file(locations)

    def read(self, id_location=None) -> Union[Optional[Location], List[Location]]:
        """
        TODO

        """

        locations = self.__read_file()
        if id_location:
            if id_location in locations:
                return locations[id_location]
            else:
                return None

        return list(locations.values())

    def update(self, location: Location) -> None:
        """
        TODO
        :param location:
        :return:
        """

        locations = self.__read_file()
        if self.read(location.id_location) is None:
            msg = f'Nu exista o locatie cu id-ul {location.id_location} de actualizat.'
            raise KeyError(msg)

        locations[location.id_location] = location
        self.__write_file(locations)

    def delete(self, id_location: str) -> None:
        """
        TODO
        :param id_location:
        :return:
        """
        locations = self.__read_file()
        if self.read(id_location) is None:
            raise KeyError(
                f'Nu exista o locatie cu id-ul {id_location} pe care sa o stergem.')

        del locations[id_location]
        self.__write_file(locations)


