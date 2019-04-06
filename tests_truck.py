"""Using Python 3.6."""

from unittest import TestCase, main

from cargo import Cargo
from truck import Truck


class TestsTruckClass(TestCase):
    def setUp(self):
        self.cargo = Cargo(
            product="Light Bulbs",
            origin_city="Sikeston",
            origin_state="MO",
            origin_lat=36.876719,
            origin_long=-89.5878759,
            destination_city="Grapevine",
            destination_state="TX",
            destination_lat=32.9342919,
            destination_long=-97.0780654,
        )

        self.truck = Truck(
            truck="Hartford Plastics Incartford",
            city="Florence",
            state="AL",
            lat=34.79981,
            lng=-87.677251,
        )

    def test_truck_truck_should_return_Hartford_Plastics_Incartford(self):
        expected = "Hartford Plastics Incartford"
        result = self.truck.truck
        self.assertEqual(result, expected)

    def test_truck_shipment_should_return_Light_Bulbs(self):
        expected = "Light Bulbs"
        result = self.truck.shipment(self.cargo)
        self.assertEqual(result, expected)

    def test_distance_between_truck_and_cargo_should_be_288_08_kilometers(
        self
    ):
        expected = 288.08
        result = self.truck.distance_to_cargo(self.cargo)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
