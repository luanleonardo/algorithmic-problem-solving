from sys import stdin, stdout


class Stack:
    def __init__(self, name):
        self._container = []
        self.name = name

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def top(self):
        return self._container[len(self._container) - 1]

    def empty(self):
        return self._container == []

    def size(self):
        return len(self._container)

    def __repr__(self):
        return repr(self._container)


def move_between(a, b, finished):

    # It is finished, if all the discs are in the destination tower.
    # In this case, do not move the discs.
    if finished:
        return None

    if a.empty() and not b.empty():
        stdout.write(f"{b.name} {a.name}" + "\n")
        a.push(b.pop())
    elif not a.empty() and b.empty():
        stdout.write(f"{a.name} {b.name}" + "\n")
        b.push(a.pop())
    else:
        if a.first() < b.first():
            stdout.write(f"{a.name} {b.name}" + "\n")
            b.push(a.pop())
        else:
            stdout.write(f"{b.name} {a.name}" + "\n")
            a.push(b.pop())


def hanoi_iterative_solver(initial_tower, auxiliary_tower, final_tower, num_discs):

    while final_tower.size() < num_discs:

        if num_discs % 2 == 0:
            move_between(
                initial_tower, auxiliary_tower, final_tower.size() == num_discs
            )
            move_between(initial_tower, final_tower, final_tower.size() == num_discs)
        else:
            move_between(initial_tower, final_tower, final_tower.size() == num_discs)
            move_between(
                initial_tower, auxiliary_tower, final_tower.size() == num_discs
            )

        move_between(auxiliary_tower, final_tower, final_tower.size() == num_discs)


def hanoi_initialize(num_discs, towers_name):

    initial_tower = Stack(towers_name[0])
    auxiliary_tower = Stack(towers_name[1])
    final_tower = Stack(towers_name[2])

    for disc in range(num_discs, 0, -1):
        initial_tower.push(disc)

    return initial_tower, auxiliary_tower, final_tower


if __name__ == "__main__":

    # Get the data
    num_boats, num_trips = map(int, stdin.readline().rstrip().split())

    # The problem is equivalent to the Hanoi tower with num_boats discs,
    # so the optimal number of trips to solve it is 2^num_boats - 1.
    num_extras_trips = num_trips - (2**num_boats - 1)

    # Test whether the problem can be solved
    if num_extras_trips >= 0:

        # It is possible to solve the problem
        stdout.write("Y" + "\n")

        # Initializes the problem with port of Portugal with num_boats.
        port_portugal, port_china, port_england = hanoi_initialize(
            num_boats, ["A", "B", "C"]
        )

        # As any solution will be accepted, we make the most of redundant trips.
        while num_extras_trips > 1:
            move_between(port_portugal, port_china, port_england.size() == num_boats)
            move_between(port_portugal, port_china, port_england.size() == num_boats)
            num_extras_trips -= 2

        # If it is necessary to make one more trip, it is done so that the next
        # three trips are part of the optimal itinerary.
        # The optimal itinerary depends on the number of boats.
        if num_extras_trips == 1:

            if num_boats % 2 == 0:
                move_between(
                    port_portugal, port_england, port_england.size() == num_boats
                )
                move_between(port_england, port_china, port_england.size() == num_boats)
                move_between(
                    port_portugal, port_england, port_england.size() == num_boats
                )
            else:
                move_between(
                    port_portugal, port_china, port_england.size() == num_boats
                )
                move_between(port_china, port_england, port_england.size() == num_boats)
                move_between(
                    port_portugal, port_china, port_england.size() == num_boats
                )

            move_between(port_china, port_england, port_england.size() == num_boats)

        # We continue to obtain the optimal itinerary, given by the iterative algorithm
        # that solves the problem of the Hanoi tower.
        hanoi_iterative_solver(port_portugal, port_china, port_england, num_boats)
    else:
        # Impossible to solve
        stdout.write("N" + "\n")
