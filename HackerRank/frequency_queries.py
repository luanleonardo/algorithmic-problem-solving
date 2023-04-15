# https://www.hackerrank.com/challenges/frequency-queries/

from collections import Counter, defaultdict

q = int(input().rstrip())

cv = Counter()
fv = defaultdict(set)
for _ in range(q):
    o, v = map(int, input().rstrip().split())
    if o == 1:
        if cv[v] > 0:
            fv[cv[v]].remove(v)
        cv[v] += 1
        fv[cv[v]].add(v)
    elif o == 2:
        if cv[v] == 0:
            continue
        fv[cv[v]].remove(v)
        cv[v] -= 1
        fv[cv[v]].add(v)
    else:
        print(f"{1 if fv[v] else 0}")
