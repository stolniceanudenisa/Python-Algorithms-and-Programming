from dataclasses import dataclass


@dataclass
class CarOrder:
    id_car_order: str
    id_car: str
    id_location: str
    final_time: float
    cost_per_km: float
    distance_traveled: float
    status: str
    