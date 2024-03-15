from dataclasses import dataclass


@dataclass
class Car:
    id_car: str
    fleet_number: str # indicativ
    comfort_level: str
    card_payment: bool
    model: str
