from typing import Dict, List

from streets.car import Car
from streets.intersection import Intersection


def create_schedules_based_on_bandwidth(cars: List[Car], intersections: Dict[int, Intersection]):
    bw_mapping = create_bandwidth_mapping(cars)
    for intersection in intersections:
        total_load = [bw_mapping[street] for street in intersection.streets]
        for street in intersection.streets:
            intersection.schedule[street]=bw_mapping[street]/total_load




def create_bandwidth_mapping(cars: List[Car]) -> Dict[int, int]:
    mapping = []
    for car in cars:
        for street_id in car.streets:
            mapping[street_id] += 1
    return mapping
