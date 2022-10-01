q = int(input().rstrip())

for _ in range(q):
    st = input().rstrip()
    S = [st[i:j] for j in range(len(st) + 1) for i in range(j)]
    d = {}
    for w in S:
        s = "".join(sorted(w))
        if s in d:
            d[s].append(w)
        else:
            d[s] = [w]
    c = [(len(d[s]) * (len(d[s]) - 1)) // 2 for s in d if len(d[s]) > 1]
    print(sum(c))
