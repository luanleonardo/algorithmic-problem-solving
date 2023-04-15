# https://www.hackerrank.com/challenges/maximum-subarray-sum/
# ref: https://stackoverflow.com/questions/31113993/maximum-subarray-sum-modulo-m
from sys import stdin, stdout


def maximum_subarray_sum_mod_m(arr, m):
    prefix_sums_mod_m = [(0, -1)]
    for i, e in enumerate(arr):
        prefix_sums_mod_m.append(((prefix_sums_mod_m[-1][0] + e) % m, i))

    prefix_sums_mod_m = sorted(prefix_sums_mod_m)
    max_seen = prefix_sums_mod_m[-1][0]

    for (a, a_idx), (b, b_idx) in zip(
        prefix_sums_mod_m[:-1], prefix_sums_mod_m[1:]
    ):
        if a_idx > b_idx and b > a:
            max_seen = max((a - b) % m, max_seen)

    return max_seen


if __name__ == "__main__":

    q = int(stdin.readline().rstrip())
    for _ in range(q):
        n, m = map(int, stdin.readline().rstrip().split())
        array = list(map(int, stdin.readline().rstrip().split()))
        stdout.write(f"{maximum_subarray_sum_mod_m(array, m)}\n")
