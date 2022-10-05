# https://www.hackerrank.com/challenges/mark-and-toys/

from sys import stdin, stdout


def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    total_price, max_num_toys = 0, 0
    for price in sorted_prices:
        if total_price + price <= k:
            total_price += price
            max_num_toys += 1

    return max_num_toys


if __name__ == "__main__":

    n, k = map(int, stdin.readline().rstrip().split())

    prices = list(map(int, stdin.readline().rstrip().split()))

    result = maximumToys(prices, k)

    stdout.write(f"{result}\n")
