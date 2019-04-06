"""Using Python 3.6."""

from unittest import TestCase, main
from cargo import Cargo


class TestsCargoClass(TestCase):
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

    def test_cargo_product_should_return_light_bulbs(self):
        expected = "Light Bulbs"
        result = self.cargo.product
        self.assertEqual(result, expected)

    def test_total_distance_to_delivery_should_be_811_20_kilometers(self):
        expected = 811.2
        result = self.cargo.total_distance_delivery()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
