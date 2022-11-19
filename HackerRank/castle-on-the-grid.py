from collections import deque, namedtuple
from sys import stdin, stdout

Location = namedtuple("Location", ["row", "column"])


def nearbyLocationsOnTheGrid(grid, free, start):
    height = len(grid)
    width = len(grid[0])
    nearbyLocations = []
    for column in range(start.column - 1, -1, -1):
        if grid[start.row][column] == free:
            nearbyLocations.append(Location(start.row, column))
        else:
            break
    for row in range(start.row - 1, -1, -1):
        if grid[row][start.column] == free:
            nearbyLocations.append(Location(row, start.column))
        else:
            break
    for column in range(start.column + 1, width):
        if grid[start.row][column] == free:
            nearbyLocations.append(Location(start.row, column))
        else:
            break
    for row in range(start.row + 1, height):
        if grid[row][start.column] == free:
            nearbyLocations.append(Location(row, start.column))
        else:
            break
    return nearbyLocations


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


def BFS(grid, free, start, goal):
    frontier = deque([Node(start, None)])
    explored = set([start])
    while frontier:
        node = frontier.pop()
        for neighbor in nearbyLocationsOnTheGrid(grid, free, node.state):
            if neighbor == goal:
                return node
            if neighbor in explored:
                continue
            explored.add(neighbor)
            frontier.appendleft(Node(neighbor, node))
    return None


def pathToGoal(node):
    reversedPath = [node.state]
    while node.parent is not None:
        node = node.parent
        reversedPath.append(node.state)
    return reversedPath[::-1]


def printGrid(grid, path):
    for loc in path:
        grid[loc.row][loc.column] = "\u25A1"

    output = ""
    for row in grid:
        output += " ".join(row) + "\n"
    print(output)


def minimumMoves(grid, free, start, goal):
    node = BFS(grid, free, start, goal)
    path = pathToGoal(node)
    printGrid(grid, path)
    return len(path)


if __name__ == "__main__":
    # get data
    n = int(stdin.readline().rstrip())
    grid = [list(stdin.readline().rstrip()) for _ in range(n)]
    startX, startY, goalX, goalY = map(int, stdin.readline().rstrip().split())

    # set variables
    start = Location(startX, startY)
    goal = Location(goalX, goalY)

    # print result
    stdout.write(f"{minimumMoves(grid, '.', start, goal)}\n")
