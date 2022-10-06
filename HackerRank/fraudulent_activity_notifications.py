# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/

from collections import deque
from sys import stdin, stdout


def get_median(sorted_array):
    l, k = len(sorted_array), len(sorted_array) // 2
    if l % 2 == 0:
        return (sorted_array[k - 1] + sorted_array[k]) / 2
    return sorted_array[k]


def partial_sorting(array):
    n = len(array)
    if n <= 1:
        return array

    key = array[-1]
    j = n - 2
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key


if __name__ == "__main__":

    n, d = map(int, stdin.readline().strip().split())
    expenditures = list(map(int, stdin.readline().strip().split()))

    q = deque()
    sorted_array = []
    notifications = 0
    for i, expenditure in enumerate(expenditures):

        if i >= d:
            median_expenditures = get_median(sorted_array)
            if expenditure >= 2 * median_expenditures:
                notifications += 1
            sorted_array.remove(q.popleft())

        q.append(expenditure)
        sorted_array.append(expenditure)
        partial_sorting(sorted_array)

    stdout.write(f"{notifications}\n")
