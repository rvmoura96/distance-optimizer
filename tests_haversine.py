"""Using Python 3.6."""

from unittest import TestCase, main
from haversine import haversine


class TestHaversineFunction(TestCase):
    def test_distance_between_sikeston_and_grapevine_should_be_811_20_kilometers(
        self
    ):
        initial_lat = 36.876719
        initial_long = -89.5878579
        destination_lat = 32.9342919
        destination_long = -97.0780654
        expected = 811.20
        result = haversine(
            initial_lat, initial_long, destination_lat, destination_long
        )
        self.assertEqual(result, expected)

    def test_distance_between_christiansburg_and_apopka_should_be_943_91_kilometers(
        self
    ):
        initial_lat = 37.1298517
        initial_long = -80.4089389
        destination_lat = 28.6934076
        destination_long = -81.5322149
        expected = 943.91
        result = haversine(
            initial_lat, initial_long, destination_lat, destination_long
        )
        self.assertEqual(result, expected)

    def test_discance_between_columbus_and_woodland_should_be_3312_14_kilometers(
        self
    ):
        initial_lat = 39.9611755
        initial_long = -82.9987942
        destination_lat = 38.6785157
        destination_long = -121.7732971
        expected = 3312.14
        result = haversine(
            initial_lat, initial_long, destination_lat, destination_long
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
