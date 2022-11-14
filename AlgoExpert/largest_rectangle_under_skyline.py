from collections import deque, namedtuple
from sys import stdin, stdout


# O(num_buildings) time | O(num_buildings) space
def largest_rectangle(buildings):
    Candidate = namedtuple("Candidate", ["index", "height"])
    left_candidates = deque([])
    largest_area = 0
    for right, height in enumerate(buildings):
        next_left = right
        while left_candidates and left_candidates[-1].height >= height:
            candidate = left_candidates.pop()
            width = right - candidate.index
            area = width * candidate.height
            largest_area = max(largest_area, area)
            next_left = candidate.index
        left_candidates.append(Candidate(next_left, height))

    return largest_area


# O(num_buildings^2) time | O(1) space
# def largest_rectangle(buildings, num_buildings):
#     largest_area = 0
#     for left in range(num_buildings):
#         height = buildings[left]
#         for right in range(left, num_buildings):
#             width = right - left + 1
#             height = min(height, buildings[right])
#             area = width * height
#             largest_area = max(largest_area, area)
#     return largest_area


def largestRectangleUnderSkyline(buildings):
    buildings.append(0)
    return largest_rectangle(buildings)


if __name__ == "__main__":
    buildings = [1, 3, 3, 2, 4, 1, 5, 3, 2]
    stdout.write(f"{largestRectangleUnderSkyline(buildings)}\n")
