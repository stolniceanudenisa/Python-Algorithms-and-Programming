from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Location(Entity):
    street_name: str
    street_number: int
