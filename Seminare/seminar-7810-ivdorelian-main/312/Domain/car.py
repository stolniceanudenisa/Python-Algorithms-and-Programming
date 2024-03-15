from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Car(Entity):
    fleet_number: str
    comfort_level: str
    model: str
