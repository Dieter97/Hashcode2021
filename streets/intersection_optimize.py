class IntersectionOptimizer:

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
        while n_sim > 0:
            for intersection in self.intersections:
                best_street = None
                best_street_score = -1
               # for street in intersection.input_streets:
                    
            n_sim -= 1

        return self.intersections