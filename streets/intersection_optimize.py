from streets.street_parser import StreetParser


class IntersectionOptimizer:

    def __init__(self, input_file):
        self.input_file = input_file
        self.parser = StreetParser()
        self.reload()
        
    def reload(self):
        problem = self.parser.parse_file(self.input_file)
        self.n_sim = problem[0]
        self.n_intersections = problem[1]
        self.n_streets = problem[2]
        self.n_cars = problem[3]
        self.bonus_point = problem[4]
        self.intersections = problem[5] 
        self.cars = problem[6] 
        self.streets = problem[7]

    def calculate_solution(self):
        pass
