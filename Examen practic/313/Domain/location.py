from dataclasses import dataclass


@dataclass
class Location:
    id_location: str
    street_name: str
    street_num: int
    block: str
    entry: str
    other_info: str



