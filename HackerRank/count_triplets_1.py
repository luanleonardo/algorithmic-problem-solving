# https://www.hackerrank.com/challenges/count-triplets-1

from collections import Counter

n, r = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

lh = Counter()
rh = Counter(arr)

ans = 0
for v in arr:

    cl = lh[v // r] if v % r == 0 else 0
    rh[v] -= 1
    cr = rh[v * r]
    lh[v] += 1
    ans += cl * cr

print(ans)
