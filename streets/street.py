import queue

class Street:

    def __init__(self, start, end, name, time):
        self.start = start
        self.end = end
        self.name = name
        self.time = time
        self.cars = queue.Queue()

