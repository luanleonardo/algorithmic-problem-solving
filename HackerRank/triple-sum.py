# https://www.hackerrank.com/challenges/triple-sum

from sys import stdin, stdout


def find_subarray_less_than_key(array, key):
    l = 0
    m = len(array) // 2
    r = len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if key < array[m]:
            r = m - 1
        elif key > array[m]:
            l = m + 1
        else:
            break
    return len(array[:m]) if key < array[m] else len(array[: m + 1])


if __name__ == "__main__":

    la, lb, lc = map(int, stdin.readline().rstrip().split())
    a, b, c = (
        sorted(set(map(int, stdin.readline().rstrip().split()))),
        sorted(set(map(int, stdin.readline().rstrip().split()))),
        sorted(set(map(int, stdin.readline().rstrip().split()))),
    )

    answer = 0
    for mid_value in b:
        res1 = find_subarray_less_than_key(array=a, key=mid_value)
        res2 = find_subarray_less_than_key(array=c, key=mid_value)
        answer += res1 * res2
    stdout.write(f"{answer}\n")
