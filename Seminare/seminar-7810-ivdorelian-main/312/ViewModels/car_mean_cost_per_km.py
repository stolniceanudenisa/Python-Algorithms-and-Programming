from dataclasses import dataclass

from Domain.car import Car


@dataclass
class CarMeanCostPerKm:
    fleet_number: str
    comfort_level: str
    mean_cost_per_km: float
