from __future__ import annotations

from typing import List

from streets.car import Car
from streets.schedule import Schedule
from streets.street import Street


class Intersection:

    def __init__(self, index):
        self.index = index
        self.input_streets: List[Street] = []
        self.output_streets: List[Street] = []
        self.schedule: List[Schedule] = []

    def get_busiest_street(self) -> Street:
        busiest = self.input_streets[0]
        for i in range(1, len(self.input_streets)):
            if busiest.cars.qsize() < self.input_streets[i].cars.qsize():
                busiest = self.input_streets[i]
        return busiest

    def is_busy(self) -> bool:
        for street in self.input_streets:
            if not street.cars.empty():
                return True
        return False

    def move_car(self, in_street: Street):
        if in_street.has_car_waiting():
            car: Car = in_street.cars.get()
            street = self.get_car_street(car)
            car.move_into_new_street(street)

    def calculate_current_schedule(self, timestep: int) -> Schedule:
        schedule = None
        for s in self.schedule:
            schedule = s
            timestep -= s.duration
            if timestep == 0:
                schedule == None
        return schedule

    # TODO verwijderen, moet dict worden
    def get_car_street(self, car) -> Street:
        for street in self.output_streets:
            for s in car.streets:
                if street.name == s.name:
                    return street
        raise Exception
