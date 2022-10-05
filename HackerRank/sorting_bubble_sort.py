# https://www.hackerrank.com/challenges/ctci-bubble-sort

from sys import stdin, stdout


def countSwaps(array):
    ans = 0
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                ans += 1
    return ans


if __name__ == "__main__":

    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split()))
    ans = countSwaps(arr)

    stdout.write(f"Array is sorted in {ans} swaps.\n")
    stdout.write(f"First Element: {arr[0]}\n")
    stdout.write(f"Last Element: {arr[n - 1]}\n")
