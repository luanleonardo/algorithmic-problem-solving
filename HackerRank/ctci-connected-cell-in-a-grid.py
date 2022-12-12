# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/

from collections import deque, Counter
from sys import stdin, stdout


def get_adjacent_cells(row, column, height, width, filled):
    return [
        (row + i, column + j)
        for (i, j) in [
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        ]
        if 0 <= row + i < height
        and 0 <= column + j < width
        and grid[row + i][column + j] == filled
    ]


def maxRegion(grid):
    height = len(grid)
    width = len(grid[0])
    filled = 1
    cc_id = 1
    cc_sizes = Counter()

    for row in range(height):
        for column in range(width):

            if grid[row][column] == filled:
                cc_id += 1
                cc_sizes[cc_id] += 1

                frontier = deque([(row, column)])
                grid[row][column] = cc_id
                while frontier:
                    cell_row, cell_column = frontier.pop()
                    for (adj_row, adj_column) in get_adjacent_cells(
                        cell_row, cell_column, height, width, filled
                    ):
                        cc_sizes[cc_id] += 1
                        grid[adj_row][adj_column] = cc_id
                        frontier.append((adj_row, adj_column))

    return cc_sizes.most_common(1)[0][1]


if __name__ == "__main__":
    rows = int(stdin.readline().strip())
    columns = int(stdin.readline().strip())
    grid = [list(map(int, stdin.readline().strip().split())) for _ in range(rows)]
    stdout.write(f"{maxRegion(grid)}\n")
