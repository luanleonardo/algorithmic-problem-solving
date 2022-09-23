# https://www.hackerrank.com/challenges/new-year-chaos/problem

from sys import stdin, stdout

t = int(stdin.readline().rstrip())

for _ in range(t):
    n = int(stdin.readline().rstrip())
    q = list(map(int, stdin.readline().rstrip().split(" ")))

    total = 0
    too_chaotic = False
    for i in range(n - 2, -1, -1):
        bribes = 0
        key = q[i]
        j = i + 1
        while j < n and q[j] < key:
            bribes += 1
            if bribes > 2:
                too_chaotic = True
                break
            q[j - 1] = q[j]
            j += 1
        if too_chaotic:
            break
        q[j - 1] = key
        total += bribes

    if too_chaotic:
        stdout.write(f"Too chaotic\n")
    else:
        stdout.write(f"{total}\n")
