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
                    #print("new schedule...")
                    # No current schedule -> calculate new one
                    buziest = intersection.get_busiest_street()
                    duration = buziest.cars.qsize()

                    if duration != 0:
                        #print("adding %s, for duration: %d" %  (buziest.name, duration))
                        intersection.schedule.append(Schedule(buziest, duration))
                else:
                    if(schedule.street.has_car_waiting()):
                        car = schedule.street.cars.get()
                        car.move_into_new_street(car.streets.pop())
                        #print(car)
                # Move the cars will move
                #[intersection.move_car(buziest) for _ in range(buziest.cars.qsize())]
            # Move simulation
            for car in self.cars:
                car.get_closer_to_end_of_street(10)
            print(self.n_sim)
            self.n_sim -= 10

        return self.intersections