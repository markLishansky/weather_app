from dataclasses import dataclass

@dataclass
class Coordinates:
    longitude: float
    latitude: float

def get_gps_coordinates() -> Coordinates:
    return Coordinates(10, 20)