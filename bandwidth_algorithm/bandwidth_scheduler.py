from typing import Dict, List

from streets.car import Car
from streets.intersection import Intersection
from streets.street import Street


def create_schedules_based_on_bandwidth(cars: List[Car], intersections: Dict[int, Intersection]):
    bw_mapping = create_bandwidth_mapping(cars)
    for intersection in intersections.values():
        total_load = [bw_mapping[street] for street in intersection.input_streets]
        for street in intersection.input_streets:
            intersection.schedule[street] = bw_mapping[street] / total_load


def create_bandwidth_mapping(cars: List[Car]) -> Dict[Street, int]:
    mapping = {}
    for car in cars:
        for street in car.streets:
            mapping[street] += 1
    return mapping
