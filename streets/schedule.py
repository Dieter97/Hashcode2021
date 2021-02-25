from streets.street import Street


class Schedule:

    def __init__(self, street: Street, duration: int):
        self.street: Street = street
        self.duration: int = duration
