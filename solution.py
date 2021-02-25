from __future__ import annotations

from typing import List

from pizza.pizza_parser import Problem, ItemLookup, ScoreCache
from tools.logging.logger_mixin import LoggerMixin


class SubSolution(object):
    def __init__(self, team_size: int, pizzas: List[int]):
        self.team_size: int = team_size
        self.pizzas: List[int] = pizzas

    def is_valid(self) -> bool:
        return len(self.pizzas) == self.team_size

    def to_string(self) -> str:
        return f"{self.team_size} {' '.join([str(pizza) for pizza in self.pizzas])}\n"

    def calculate_score(self, score_cache: ScoreCache):
        return score_cache.cache[tuple(self.pizzas)]


class Solution(LoggerMixin):
    def __init__(self, problem: Problem):
        self.sub_solutions: List[SubSolution] = []
        self.problem = problem

    # Todo
    # Adds a new item to the solution if constructing solutions
    def add(self, sub_solution: SubSolution) -> None:
        self.sub_solutions.append(sub_solution)

    # Todo
    # Calculates some sort of efficiency metric for comparing solutions
    def calculate_score(self) -> int:
        return sum(sub_sol.calculate_score(self.problem.score_cache) for sub_sol in self.sub_solutions)

    # Todo
    # Used to check if the solution is valid, so that algorithms can fail early
    def is_valid(self) -> bool:
        pass

    def auto_write(self):
        self.write()

    def write(self, solution_file_name: str):
        #        assert len(self.team_sizes) == len(self.pizzas), "Incomplete solution!"
        with open(solution_file_name, 'w') as output_file:
            output_file.write(f"{len(self.sub_solutions)}\n")
            for sub_solution in self.sub_solutions:
                output_file.write(sub_solution.to_string())

    # Todo
    # Used for printing a solution, useful with long-running solvers who find intermediate, possibly better solutions
    def __str__(self) -> str:
        pass

    # Todo
    # Required when making deep copies of a solution
    def __deepcopy__(self, memodict=None) -> Solution:
        if memodict is None:
            memodict = {}
        return Solution()
