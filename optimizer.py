"""Using Python 3.6."""

import csv
from pprint import pprint

from cargo import Cargo
from truck import Truck


cargo_list = list()
trucks_list = list()
optimum_choices = dict()

# Read all cargo csv and create a Cargo instance for each input
with open("cargo.csv") as cargo_file:
    cargos = csv.reader(cargo_file)
    next(cargos)
    for c in cargos:
        cargo_list.append(
            Cargo(
                product=c[0],
                origin_city=c[1],
                origin_state=c[2],
                origin_lat=float(c[3]),
                origin_long=float(c[4]),
                destination_city=c[5],
                destination_state=c[6],
                destination_lat=float(c[7]),
                destination_long=float(c[8]),
            )
        )

# Read all trucks csv and create a Truck instance for each input
with open("trucks.csv") as trucks_file:
    trucks = csv.reader(trucks_file)
    next(trucks)
    for t in trucks:
        trucks_list.append(
            Truck(
                truck=t[0],
                city=t[1],
                state=t[2],
                lat=float(t[3]),
                lng=float(t[4]),
            )
        )

# Iterate between cargo_list and truck_list searching for the best choice
# to deliver each cargo. The best choice should be the lowest distance
# between a cargo and a truck.
for c in cargo_list:
    best_choice = trucks_list[0]
    optimal_distance = best_choice.distance_to_cargo(c)
    for t in trucks_list:
        if t.distance_to_cargo(c) < optimal_distance:
            optimal_distance = t.distance_to_cargo(c)
            best_choice = t
    optimum_choices[c.product] = {
        "truck": best_choice.truck,
        "total-distance-km": round(
            optimal_distance + c.total_distance_delivery(), ndigits=2
        ),
    }
    trucks_list.remove(best_choice)

pprint(optimum_choices)
