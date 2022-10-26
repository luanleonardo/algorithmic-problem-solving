# https://www.hackerrank.com/challenges/maximum-subarray-sum/
# ref: https://stackoverflow.com/questions/31113993/maximum-subarray-sum-modulo-m
from sys import stdin, stdout


def maximum_subarray_sum_module_m(array, m):
    prefix_sums = [(0, -1)]
    for i, e in enumerate(array):
        prefix_sums.append(((prefix_sums[-1][0] + e) % m, i))

    prefix_sums = sorted(prefix_sums)
    max_seen = prefix_sums[-1][0]

    for (array, a_idx), (b, b_idx) in zip(prefix_sums[:-1], prefix_sums[1:]):
        if a_idx > b_idx and b > array:
            max_seen = max((array - b) % m, max_seen)

    return max_seen


if __name__ == "__main__":

    q = int(stdin.readline().rstrip())
    for _ in range(q):
        n, m = map(int, stdin.readline().rstrip().split())
        array = list(map(int, stdin.readline().rstrip().split()))
        answer = maximum_subarray_sum_module_m(array, m)
        stdout.write(f"{answer}\n")
