# https://www.algoexpert.io/questions/non-constructible-change


# O(N * log N) time | O(1) space, N = number of coins
def nonConstructibleChange(coins):
    min_change_cant_create = 1
    if not coins:
        return min_change_cant_create
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        if coin <= min_change_cant_create:
            min_change_cant_create += coin
    return min_change_cant_create


if __name__ == "__main__":
    print(nonConstructibleChange(coins=[5, 7, 1, 1, 2, 3, 22]))
