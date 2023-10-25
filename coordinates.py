from dataclasses import dataclass
from subprocess import Popen, PIPE
from typing import Literal
import geocoder
import config
from exceptions import CantGetCoordinates

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    coordinates = _get_geocoder_coordinates()
    return _round_coordinates(coordinates)

def _get_geocoder_coordinates() -> Coordinates:
    whereami_output = _get_geocoder_output()
    coordinates = _parse_coordinates(whereami_output)
    return coordinates

def _get_geocoder_output() -> str:
    location = geocoder.ip('me')
    
    if location.ok and location.latlng:
        latitude, longitude = location.latlng
        output_str = f"Latitude: {latitude}, Longitude: {longitude}"
        return output_str 
    else:
        raise CantGetCoordinates

def _parse_coordinates(coordinates_str: str) -> Coordinates:
    parts = coordinates_str.strip().split(", ")
    if len(parts) == 2:
        latitude_str, longitude_str = parts
        latitude = _parse_float_coordinate(latitude_str.split(":")[1])
        longitude = _parse_float_coordinate(longitude_str.split(":")[1])
        return Coordinates(latitude, longitude)
    else:
        raise CantGetCoordinates

def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())

