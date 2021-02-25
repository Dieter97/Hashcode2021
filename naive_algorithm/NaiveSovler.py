from streets.schedule import Schedule
from streets.intersection_optimize import IntersectionOptimizer


class NaiveIntersectionOptimizer(IntersectionOptimizer):

    def __init__(self, input_file):
        super().__init__(input_file)

    def calculate_solution(self):
        #while self.n_sim > 0:
        for index, intersection in self.intersections.items():
            while len(intersection.input_streets) > 0:
                buziest = intersection.input_streets.pop()
                
                duration = max(1,buziest.cars.qsize())

                #if duration != 0:
                    #print("adding %s, for duration: %d" %  (buziest.name, duration))
                intersection.schedule.append(Schedule(buziest, duration))

                        #print(car)
                # Move the cars will move
                #[intersection.move_car(buziest) for _ in range(buziest.cars.qsize())]
            # Move simulation
            #for car in self.cars:
            #    car.get_closer_to_end_of_street(10)
            #print(self.n_sim)
           # self.n_sim -= 10

        return self.intersections