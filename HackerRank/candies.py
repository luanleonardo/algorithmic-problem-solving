# https://www.hackerrank.com/challenges/candies

from sys import stdin, stdout

# O(n) time | O(n) space
def candies(n, rating):
    candies = [1] * n
    for i in range(n - 1):
        if rating[i] < rating[i + 1]:
            candies[i + 1] = candies[i] + 1
    for i in reversed(range(n - 1)):
        if rating[i] > rating[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
    return sum(candies)


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    rating = [int(stdin.readline().rstrip()) for _ in range(n)]
    stdout.write(f"{candies(n, rating)}\n")
