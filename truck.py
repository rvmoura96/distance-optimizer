"""Using Python 3.6."""

from cargo import Cargo
from haversine import haversine


class Truck:
    def __init__(
        self, truck: str, city: str, state: str, lat: float, lng: float
    ) -> None:
        self.truck = truck
        self.city = city
        self.state = state
        self.lat = lat
        self.long = lng

    def shipment(self, cargo: Cargo) -> str:
        return cargo.product

    def distance_to_cargo(self, cargo: Cargo) -> float:
        distance_to_cargo = haversine(
            self.lat, self.long, cargo.origin_lat, cargo.origin_long
        )
        return distance_to_cargo
