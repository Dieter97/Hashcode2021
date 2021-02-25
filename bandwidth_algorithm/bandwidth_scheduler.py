from math import floor
from typing import Dict, List

from streets.car import Car
from streets.intersection import Intersection
from streets.intersection_optimize import IntersectionOptimizer
from streets.schedule import Schedule
from streets.street import Street


class BandwidthScheduler(IntersectionOptimizer):

    def calculate_solution(self):

        self.create_schedules_based_on_bandwidth(self.cars, self.intersections)

    @staticmethod
    def create_schedules_based_on_bandwidth(cars: List[Car], intersections: Dict[int, Intersection]):
        bw_mapping = BandwidthScheduler.create_bandwidth_mapping(cars)
        for intersection in intersections.values():
            total_load = sum([bw_mapping[street] for street in intersection.input_streets])
            for street in intersection.input_streets:
                schedule = Schedule(street, floor(bw_mapping[street] / total_load))
                intersection.schedule.append(schedule)

    @staticmethod
    def create_bandwidth_mapping(cars: List[Car]) -> Dict[Street, int]:
        mapping = {}
        for car in cars:
            for street in car.streets:
                mapping[street] += 1
        return mapping
