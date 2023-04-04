# https://www.algoexpert.io/questions/tournament-winner
from collections import Counter


# O(M) time | O(N) space, M = number of competitions, N = number of teams
def tournamentWinner(competitions, results):
    points = Counter()
    for (home_team, away_team), result in zip(competitions, results):
        points[home_team] += result
        points[away_team] += 1 - result
    return points.most_common(1)[0][0]


if __name__ == "__main__":
    competitions = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = [0, 1, 1]
    print(tournamentWinner(competitions, results))
