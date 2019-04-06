"""Using Python 3.6."""
from math import radians, cos, sin, sqrt, atan2


def haversine(
    initial_lat: float,
    initial_long: float,
    destination_lat: float,
    destination_long: float,
) -> float:
    """Return the delta betwen to points in km.

    It returns the delta betwen two points on earth using haversine formula.
    """
    EARTH_RADIUS_KM = 6371

    initial_lat, initial_long, destination_lat, destination_long = map(
        radians, [initial_lat, initial_long, destination_lat, destination_long]
    )

    delta_lat = destination_lat - initial_lat
    delta_long = destination_long - initial_long
    a = (
        sin(delta_lat / 2) ** 2
        + cos(initial_lat) * cos(destination_lat) * sin(delta_long / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = EARTH_RADIUS_KM * c
    return round(distance, ndigits=2)