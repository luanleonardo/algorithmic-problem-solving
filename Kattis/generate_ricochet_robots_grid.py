from __future__ import annotations
import random
from collections import defaultdict
from enum import Enum
from typing import NamedTuple, List
from sys import stdin, stdout


class Cell(str, Enum):
    EMPTY = "."
    GOAL = "X"
    PATH = "*"
    ROBOT_ONE = "1"
    ROBOT_TWO = "2"
    ROBOT_THREE = "3"
    ROBOT_FOUR = "4"
    WALL = "W"


class CellLocation(NamedTuple):
    row: int
    column: int


class FactoryFloor:
    def __init__(
        self,
        n: int = 4,
        rows: int = 10,
        columns: int = 10,
        sparseness: float = 0.25,
    ) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.number_of_robots: int = n
        self.goal: CellLocation = CellLocation(
            random.randint(0, rows - 1), random.randint(0, columns - 1)
        )
        self.robots: defaultdict[str, CellLocation] = defaultdict(CellLocation)

        # preenche o grid com células vazias
        self.grid: List[List[Cell]] = [
            [Cell.EMPTY for _ in range(columns)] for _ in range(rows)
        ]

        # preenche o grid com paredes, alvo e robôs
        self._randomly_fill_walls(rows, columns, sparseness)
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL
        self._randomly_fill_robots(rows, columns)

    def _randomly_fill_robots(self, rows, columns):
        robot_number = {
            "1": Cell.ROBOT_ONE,
            "2": Cell.ROBOT_TWO,
            "3": Cell.ROBOT_THREE,
            "4": Cell.ROBOT_FOUR,
        }
        for i in range(1, self.number_of_robots + 1):
            while True:
                cl = CellLocation(
                    random.randint(0, rows - 1), random.randint(0, columns - 1)
                )
                if self.grid[cl.row][cl.column] == Cell.EMPTY:
                    self.robots[str(i)] = cl
                    self.grid[cl.row][cl.column] = robot_number[str(i)]
                    break

    def _randomly_fill_walls(self, rows: int, columns: int, sparseness: float) -> None:
        for row in range(rows):
            for column in range(columns):
                # 20% das células do grid serão bloqueadas
                if random.uniform(0.0, 1.0) < sparseness:
                    self.grid[row][column] = Cell.WALL

    def goal_test(self, ml: CellLocation) -> bool:
        return ml == self.goal

    def ricocheting_moves(self, ml: CellLocation) -> List[CellLocation]:
        locations: List[CellLocation] = []
        free_locations: List[CellLocation] = []
        for column in range(ml.column - 1, -1, -1):
            if self.grid[ml.row][column] in [
                Cell.WALL,
                Cell.ROBOT_ONE,
                Cell.ROBOT_TWO,
                Cell.ROBOT_THREE,
                Cell.ROBOT_FOUR,
            ]:
                break
            free_locations.append(CellLocation(ml.row, column))

        if free_locations:
            locations.append(free_locations.pop())
            free_locations: List[CellLocation] = []

        for row in range(ml.row - 1, -1, -1):
            if self.grid[row][ml.column] in [
                Cell.WALL,
                Cell.ROBOT_ONE,
                Cell.ROBOT_TWO,
                Cell.ROBOT_THREE,
                Cell.ROBOT_FOUR,
            ]:
                break
            free_locations.append(CellLocation(row, ml.column))

        if free_locations:
            locations.append(free_locations.pop())
            free_locations: List[CellLocation] = []

        for column in range(ml.column + 1, self._columns):
            if self.grid[ml.row][column] in [
                Cell.WALL,
                Cell.ROBOT_ONE,
                Cell.ROBOT_TWO,
                Cell.ROBOT_THREE,
                Cell.ROBOT_FOUR,
            ]:
                break
            free_locations.append(CellLocation(ml.row, column))

        if free_locations:
            locations.append(free_locations.pop())
            free_locations: List[CellLocation] = []

        for row in range(ml.row + 1, self._rows):
            if self.grid[row][ml.column] in [
                Cell.WALL,
                Cell.ROBOT_ONE,
                Cell.ROBOT_TWO,
                Cell.ROBOT_THREE,
                Cell.ROBOT_FOUR,
            ]:
                break
            free_locations.append(CellLocation(row, ml.column))

        if free_locations:
            locations.append(free_locations.pop())

        return locations

    def mark(self, path: List[CellLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[CellLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = ""
        for row in self.grid:
            output += " ".join([c.value for c in row]) + "\n"
        return output


if __name__ == "__main__":

    num_robots = 3  # random.randint(2, 4)
    num_rows = 5  # random.randint(4, 9)
    num_columns = 5  # random.randint(5, 9)

    floor: FactoryFloor = FactoryFloor(n=num_robots, rows=num_rows, columns=num_columns)

    output: str = ""
    for row in floor.grid:
        output += "".join([c.value for c in row]) + "\n"

    stdout.write(" ".join([str(num_robots), str(num_rows), str(num_columns)]) + "\n")
    stdout.write(output)
