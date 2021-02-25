from __future__ import annotations

from typing import List

from streets.street import Street


class Car:

    def __init__(self, n_streets, streets):
        self.n_streets: int = n_streets
        self.streets: List[int] = streets
        self.time_from_end_of_street: int = 0
        self.current_street_index: int = 0

    def is_at_end_of_street(self) -> bool:
        return self.time_from_end_of_street == 0

    def get_closer_to_end_of_street(self) -> None:
        if self.time_from_end_of_street > 0:
            self.time_from_end_of_street -= 1

    def move_into_new_street(self, street: Street):
        self.time_from_end_of_street = street.time
        self.current_street_index += 1

    def has_arrived(self):
        return self.current_street_index == self.n_streets
