from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class CarOrder(Entity):
    id_car: str
    id_location: str
    cost_per_km: float
