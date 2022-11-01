# https://www.hackerrank.com/challenges/minimum-time-required
# ref: https://www.geeksforgeeks.org/minimum-time-required-produce-m-items/

# Method 2 (efficient):
# The idea is to use Binary Search.
# Maximum possible time required to produce m items will be
# maximum time in the array, amax, multiplied by m i.e amax * m. So,
# use binary search between 1 to amax * m and find the minimum time
# which produce m items.

#  Below is the implementation of the above idea :
# Efficient Python3 program to find
# minimum time required to produce m items.
from sys import maxsize, stdin, stdout


def findItems(arr, n, temp):
    ans = 0
    for i in range(n):
        ans += temp // arr[i]
    return ans


# Binary search to find minimum time
# required to produce M items.
def bs(arr, n, m, high):
    low = 1

    # Doing binary search to find minimum
    # time.
    while low < high:

        # Finding the middle value.
        mid = (low + high) >> 1

        # Calculate number of items to
        # be produce in mid sec.
        itm = findItems(arr, n, mid)

        # If items produce is less than
        # required, set low = mid + 1.
        if itm < m:
            low = mid + 1

        # Else set high = mid.
        else:
            high = mid
    return high


# Return the minimum time required to
# produce m items with given machine.
def minTime(arr, n, m):
    maxval = -maxsize

    # Finding the maximum time in the array.
    for i in range(n):
        maxval = max(maxval, arr[i])

    return bs(arr, n, m, maxval * m)


if __name__ == "__main__":

    n, goal = map(int, stdin.readline().rstrip().split())
    machines = list(map(int, stdin.readline().rstrip().split()))
    answer = minTime(machines, n, goal)
    stdout.write(f"{answer}\n")
