# https://www.hackerrank.com/challenges/mark-and-toys/

from sys import stdin, stdout


def maximumToys(prices, k):
    total_price = 0
    sorted_prices = sorted(prices)
    for max_num_toys, price in enumerate(sorted_prices):
        if total_price + price > k:
            break
        total_price += price
    return max_num_toys


if __name__ == "__main__":

    n, k = map(int, stdin.readline().rstrip().split())
    prices = list(map(int, stdin.readline().rstrip().split()))
    result = maximumToys(prices, k)
    stdout.write(f"{result}\n")
