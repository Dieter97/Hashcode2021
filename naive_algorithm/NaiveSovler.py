from streets.schedule import Schedule
from streets.intersection_optimize import IntersectionOptimizer


class NaiveIntersectionOptimizer(IntersectionOptimizer):

    def __init__(self, input_file):
        super().__init__(input_file)

    def calculate_solution(self):
        while self.n_sim > 0:
            for index, intersection in self.intersections.items():
                schedule = intersection.calculate_current_schedule(self.n_sim)
                if schedule == None:
                    print("new schedule...")
                    # No current schedule -> calculate new one
                    buziest = intersection.get_busiest_street()

                    duration = buziest.cars.qsize()

                    if duration != 0:
                        #print("adding %s, for duration: %d" %  (buziest.name, duration))
                        intersection.schedule.append(Schedule(buziest, duration))
                else:
                    print("exisiting schedule...")
                    intersection.move_car(schedule.street)
                # Move the cars will move
                #[intersection.move_car(buziest) for _ in range(buziest.cars.qsize())]
            # Move simulation
            for car in self.cars:
                car.get_closer_to_end_of_street()

            self.n_sim -= 1            

        return self.intersections