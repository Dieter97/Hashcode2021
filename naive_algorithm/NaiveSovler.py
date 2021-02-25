from streets.schedule import Schedule

class NaiveIntersectionOptimizer:

    def __init__(self, problem):
        self.n_sim = problem[0]
        self.n_intersections = problem[1]
        self.n_streets = problem[2]
        self.n_cars = problem[3]
        self.bonus_point = problem[4]
        self.intersections = problem[5] 
        self.cars = problem[6] 
        self.streets = problem[7]

    def calculate_solution(self):
        #while self.n_sim > 0:
        for index, intersection in self.intersections.items():

            buziest = intersection.get_busiest_street()

            duration = buziest.cars.qsize()

            intersection.schedule.append(Schedule(buziest, duration))

            # Move the cars will move
            #[intersection.move_car(buziest) for _ in range(buziest.cars.qsize())]
                    
            #self.n_sim -= 1            

        return self.intersections