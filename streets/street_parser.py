from streets.street import Street
from streets.intersection import Intersection
from streets.car import Car

class StreetParser:

    def __init__(self):
        super().__init__()

    def parse_file(self,input_file):
        f = open(input_file)
        
        n_sim, n_intersections, n_streets, n_cars, bonus_point = (int(s) for s in f.readline().split())
        intersections = {}
        cars = []
        streets = {}
        i = 0
        for line in f:
            info = line.split()
            if i < n_streets:
                street = Street(int(info[0]),int(info[1]),info[2],int(info[3]))
                streets[street.name] = street
                if not street.start in intersections.keys():
                    intersections[street.start] = Intersection(street.start)
                intersections[street.start].output_streets.append(street)

                if not street.end in intersections.keys():
                    intersections[street.end] = Intersection(street.end)
                intersections[street.end].input_streets.append(street)
            else:
                start = info[1]
                car = Car(int(info[0]))
                for s in info[2:]:
                    car.streets.append(streets[s])
                streets[start].cars.put(car)
                car.streets.reverse()
                cars.append(car)
            i += 1

        cars.sort(key=lambda x: x.n_streets, reverse=False)
        return n_sim, n_intersections, n_streets, n_cars, bonus_point, intersections, cars, streets
