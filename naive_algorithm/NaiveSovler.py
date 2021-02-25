from streets.schedule import Schedule
from streets.intersection_optimize import IntersectionOptimizer


class NaiveIntersectionOptimizer(IntersectionOptimizer):

    def __init__(self, input_file):
        super().__init__(input_file)

    def calculate_solution(self):
            
        for index, intersection in self.intersections.items():

            buziest = intersection.get_busiest_street()

            duration = self.n_sim

            if duration != 0:
                intersection.schedule.append(Schedule(buziest, duration))
                              
        return self.intersections