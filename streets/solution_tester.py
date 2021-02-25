from typing import Dict, List

from streets.car import Car
from streets.intersection import Intersection


def test_solution(cars: List[Car], intersections: Dict[int, Intersection], simulation_time: int) -> int:
    working_car_list = cars.copy()
    total_reward = 0
    for timestep in range(simulation_time):
        new_working_car_list = []
        for car in working_car_list:
            car.get_closer_to_end_of_street()
            if car.has_arrived():
                total_reward += 1000 + simulation_time - timestep
            else:
                new_working_car_list.append(car)

        for intersection in intersections.values():
            if intersection.is_busy():
                street_index = intersection.calculate_current_schedule(timestep)
                intersection.move_car(intersection.input_streets[street_index])
        working_car_list = [car for car in working_car_list if not car.has_arrived()]
    return total_reward
