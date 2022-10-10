# https://www.hackerrank.com/challenges/common-child/
# https://www.programiz.com/dsa/longest-common-subsequence
# CLRS Secs 15.4
from sys import stdin, stdout


def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


s1 = stdin.readline().strip()
s2 = stdin.readline().strip()

stdout.write(f"{lcs_length(s1, s2)}\n")
