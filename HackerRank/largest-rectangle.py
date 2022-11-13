# https://www.hackerrank.com/challenges/largest-rectangle

from collections import deque, namedtuple
from sys import stdin, stdout


def largest_rectangle(skyline, num_buildings):
    Candidate = namedtuple("Candidate", ["index", "height"])
    left_candidates = deque([])
    largest_area = 0
    for right in range(num_buildings):
        height = skyline[right]
        last_index = right
        while left_candidates and left_candidates[-1].height >= height:
            candidate = left_candidates.pop()
            width = right - candidate.index
            area = width * candidate.height
            largest_area = max(largest_area, area)
            last_index = candidate.index
        left_candidates.append(Candidate(last_index, height))
    return largest_area


if __name__ == "__main__":
    num_buildings = int(stdin.readline().rstrip()) + 1
    skyline = list(map(int, stdin.readline().rstrip().split())) + [0]
    stdout.write(f"{largest_rectangle(skyline, num_buildings)}")
