import queue


class Street:

    def __init__(self, start, end, name, time):
        self.start = start
        self.end = end
        self.name = name
        self.time = time
        self.cars: queue.Queue = queue.Queue()

    def has_car_waiting(self) -> bool:
        if self.cars.qsize() == 0:
            return False
        return self.cars.queue[0].is_at_end_of_street()
