from sys import stdin, stdout


def longest_common_subsequence(x, y):
    n = len(x)
    m = len(y)

    A = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                A[i + 1][j + 1] = A[i][j] + 1
            else:
                A[i + 1][j + 1] = max(A[i][j + 1], A[i + 1][j])

    sol = []
    i, j = n, m
    while A[i][j] > 0:
        if A[i][j] == A[i - 1][j]:
            i -= 1
        elif A[i][j] == A[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            sol.append(x[i])
    return "".join(sol[::-1])


s1 = stdin.readline().strip()
s2 = stdin.readline().strip()
common_child = longest_common_subsequence(s1, s2)


stdout.write(f"{len(common_child)}\n")
