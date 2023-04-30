# https://www.algoexpert.io/questions/stable-internships

from collections import deque


def stable_matching(men, women):
    """Stable matching by Gale-Shapley"""
    n = len(men)
    propose = [0] * n
    matching = [None] * n

    rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for m in range(n):
            rank[w][women[w][m]] = m

    singles = deque(range(n))
    while singles:
        m = singles.popleft()
        w = men[m][propose[m]]
        propose[m] += 1
        if matching[w] is None:
            matching[w] = m
        elif rank[w][m] < rank[w][matching[w]]:
            singles.append(matching[w])
            matching[w] = m
        else:
            singles.append(m)

    return matching


# O(n^2) time | O(n^2) space, n = number of men
def stableInternships(interns, teams):
    return [
        [m, w] for w, m in enumerate(stable_matching(men=interns, women=teams))
    ]
