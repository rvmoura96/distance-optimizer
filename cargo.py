"""Using Python 3.6."""

from haversine import haversine


class Cargo:
    def __init__(
        self,
        product: str,
        origin_city: str,
        origin_state: str,
        origin_lat: float,
        origin_long: float,
        destination_city: str,
        destination_state: str,
        destination_lat: float,
        destination_long: float,
    ) -> None:
        self.product = product
        self.origin_city = origin_city
        self.origin_state = origin_state
        self.origin_lat = origin_lat
        self.origin_long = origin_long
        self.destination_city = destination_city
        self.destination_state = destination_state
        self.destination_lat = destination_lat
        self.destination_long = destination_long

    def total_distance_delivery(self) -> float:
        """Return the distance in KM betwen the cargo and destination."""
        return haversine(
            self.origin_lat,
            self.origin_long,
            self.destination_lat,
            self.destination_long,
        )


if __name__ == "__main__":
    pass
