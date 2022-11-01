# https://www.hackerrank.com/challenges/triple-sum

from sys import stdin, stdout


def count_values_less_than_or_equal_to_key(array, key):
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
    return m if key < array[m] else m + 1


if __name__ == "__main__":

    la, lb, lc = map(int, stdin.readline().rstrip().split())
    a, b, c = (
        sorted(set(map(int, stdin.readline().rstrip().split()))),
        sorted(set(map(int, stdin.readline().rstrip().split()))),
        sorted(set(map(int, stdin.readline().rstrip().split()))),
    )

    answer = 0
    for mid_value in b:
        res1 = count_values_less_than_or_equal_to_key(array=a, key=mid_value)
        res2 = count_values_less_than_or_equal_to_key(array=c, key=mid_value)
        answer += res1 * res2
    stdout.write(f"{answer}\n")
