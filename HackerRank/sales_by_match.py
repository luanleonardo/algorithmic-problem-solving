from sys import stdin, stdout


def sockMerchant(n, ar):
    c = {}
    for e in ar:
        if e not in c:
            c[e] = 0
        c[e] += 1

    return sum(t // 2 for t in c.values())


if __name__ == "__main__":

    n = int(stdin.readline().rstrip())

    ar = list(map(int, stdin.readline().rstrip().split()))

    result = sockMerchant(n, ar)

    stdout.write(str(result) + "\n")
