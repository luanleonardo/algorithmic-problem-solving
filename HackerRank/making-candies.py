# https://www.hackerrank.com/challenges/making-candies
# ref: https://youtu.be/bMetMg5QHzM

from math import ceil
from sys import stdin, stdout


def minimumPasses(m, w, p, n):
    days = 0
    candies = 0
    answer = ceil(n / (m * w))

    while days < answer:
        if p > candies:
            daysNeeded = ceil((p - candies) / (m * w))
            candies += daysNeeded * m * w
            days += daysNeeded

        diff = abs(m - w)
        available = candies // p
        purchased = min(diff, available)

        if m < w:
            m += purchased
        else:
            w += purchased

        rest = available - purchased
        m += rest // 2
        w += rest - rest // 2
        candies -= available * p

        candies += m * w
        days += 1

        remainingCandies = max(n - candies, 0)
        answer = min(answer, days + ceil(remainingCandies / (m * w)))

    return answer


if __name__ == "__main__":
    m, w, p, n = map(int, stdin.readline().rstrip().split())
    stdout.write(f"{minimumPasses(m, w, p, n)}\n")
