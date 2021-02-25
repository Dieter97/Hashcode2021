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
        return self.intersections

    @staticmethod
    def create_schedules_based_on_bandwidth(cars: List[Car], intersections: Dict[int, Intersection]):
        bw_mapping = BandwidthScheduler.create_bandwidth_mapping(cars)
        for intersection in intersections.values():
            total_load = sum([bw_mapping[street] if street in bw_mapping else 0 for street in intersection.input_streets])
            if total_load == 0:
                continue
            for street in intersection.input_streets:
                if street in bw_mapping:
                    schedule = Schedule(street, floor(bw_mapping[street] / total_load))
                    intersection.schedule.append(schedule)

    @staticmethod
    def create_bandwidth_mapping(cars: List[Car]) -> Dict[Street, int]:
        mapping={}
        for car in cars:
            for street in car.streets:
                if street not in mapping:
                    mapping[street]=0
                else:
                    mapping[street] += 1
        return mapping
