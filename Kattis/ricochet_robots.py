"""
https://open.kattis.com/problems/ricochetrobots
"""
from __future__ import annotations

from collections import deque
from sys import stdin, stdout
from typing import List, NamedTuple, Optional, Callable, TypeVar, Generic

T = TypeVar("T")


class Location(NamedTuple):
    row: int
    column: int


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node]) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent


def find_all_available_locations(
    robot_location: List[Location],
) -> List[List[Location]]:
    """
    Find all available locations for each robot from the current location.
    """
    robots_available_locations: List[List[Location]] = []

    for current_robot_location in robot_location:
        available_locations: List[Location] = []

        # find available locations on the left
        left_locations = find_left_locations(current_robot_location, robot_location)
        if left_locations:
            available_locations.append(left_locations.pop())

        # find available locations above
        above_locations = find_above_locations(current_robot_location, robot_location)
        if above_locations:
            available_locations.append(above_locations.pop())

        # find available locations on the right
        right_locations = find_right_locations(current_robot_location, robot_location)
        if right_locations:
            available_locations.append(right_locations.pop())

        # find available locations below
        below_locations = find_below_locations(current_robot_location, robot_location)
        if below_locations:
            available_locations.append(below_locations.pop())

        robots_available_locations.append(available_locations)

    return robots_available_locations


def find_below_locations(current_robot_location, robot_location):
    below_locations: List[Location] = []
    for grid_row in range(current_robot_location.row + 1, num_rows):
        if (
            Location(grid_row, current_robot_location.column) in robot_location
            or grid[grid_row][current_robot_location.column] == cell["WALL"]
        ):
            break
        below_locations.append(Location(grid_row, current_robot_location.column))
    return below_locations


def find_right_locations(current_robot_location, robot_location):
    right_locations: List[Location] = []
    for grid_column in range(current_robot_location.column + 1, num_columns):
        if (
            Location(current_robot_location.row, grid_column) in robot_location
            or grid[current_robot_location.row][grid_column] == cell["WALL"]
        ):
            break
        right_locations.append(Location(current_robot_location.row, grid_column))
    return right_locations


def find_above_locations(current_robot_location, robot_location):
    above_locations: List[Location] = []
    for grid_row in range(current_robot_location.row - 1, -1, -1):
        if (
            Location(grid_row, current_robot_location.column) in robot_location
            or grid[grid_row][current_robot_location.column] == cell["WALL"]
        ):
            break
        above_locations.append(Location(grid_row, current_robot_location.column))
    return above_locations


def find_left_locations(current_robot_location, robot_location):
    left_locations: List[Location] = []
    for grid_column in range(current_robot_location.column - 1, -1, -1):
        if (
            Location(current_robot_location.row, grid_column) in robot_location
            or grid[current_robot_location.row][grid_column] == cell["WALL"]
        ):
            break
        left_locations.append(Location(current_robot_location.row, grid_column))
    return left_locations


def find_all_possible_locations(
    robots_current_location: List[Location],
) -> List[List[Location]]:
    """
    Find all possible robot locations starting from the current one.
    """
    available_locations: List[List[Location]] = find_all_available_locations(
        robots_current_location
    )
    robot_locations: List[List[Location]] = []

    for robot_number in range(num_robots):
        location = robots_current_location[:]

        while available_locations[robot_number]:
            location[robot_number] = available_locations[robot_number].pop()
            robot_locations.append(location[:])

    return robot_locations


def test_target(location: List[Location]) -> bool:
    """
    Test whether the location of the first robot is the same as the target.
    """
    return location[0] == target_location


def bfs(
    initial_state: T,
    goal_test: Callable[[T], bool],
    successors: Callable[[T], List[T]],
) -> Optional[Node[T]]:
    """
    Breadth-first search algorithm.
    """
    to_visit: deque[Node[T]] = deque()
    to_visit.append(Node(initial_state, None))
    explored: List[T] = [initial_state]

    while to_visit:
        current_node: Node[T] = to_visit.popleft()
        current_node_state: T = current_node.state

        if goal_test(current_node_state):
            return current_node

        for child in successors(current_node_state):
            if child not in explored:
                explored.append(child)
                to_visit.append(Node(child, current_node))
    return None


def node_to_path(node: Node[T]) -> List[T]:
    """
    Given a node, it goes through all its
    parents, returning the path to the
    given node.
    """
    path: List[T] = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


if __name__ == "__main__":

    cell = {
        "EMPTY": ".",
        "WALL": "W",
        "TARGET": "X",
        "ROBOT_ONE": "1",
        "ROBOT_TWO": "2",
        "ROBOT_THREE": "3",
        "ROBOT_FOUR": "4",
    }

    # read first line of input
    num_robots, num_columns, num_rows, upper_bound_of_moves = map(
        int, stdin.readline().rstrip().split()
    )

    # initialize variables
    target_location: Location = Location(-1, -1)
    robots_initial_location: List[Location] = [
        Location(-1, -1) for _ in range(num_robots)
    ]
    grid: List[List[str]] = [
        [cell["EMPTY"] for _ in range(num_columns)] for _ in range(num_rows)
    ]

    # read data from grid
    for r in range(num_rows):
        row = list(stdin.readline().rstrip())
        for c in range(num_columns):
            if row[c] in [
                cell["ROBOT_ONE"],
                cell["ROBOT_TWO"],
                cell["ROBOT_THREE"],
                cell["ROBOT_FOUR"],
            ]:
                robots_initial_location[int(row[c]) - 1] = Location(r, c)
                grid[r][c] = cell["EMPTY"]
                continue
            elif row[c] == cell["TARGET"]:
                target_location = Location(r, c)
            grid[r][c] = row[c]

    # Search for solution using breadth-first search algorithm
    solution = bfs(robots_initial_location, test_target, find_all_possible_locations)
    if solution is None:
        stdout.write("NO SOLUTION" + "\n")
    else:
        solution_path = node_to_path(solution)
        solution_path_length = len(solution_path) - 1
        if upper_bound_of_moves < solution_path_length:
            stdout.write("NOT ACCEPTABLE SOLUTION" + "\n")
        else:
            stdout.write(str(solution_path_length) + "\n")
