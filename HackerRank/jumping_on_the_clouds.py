n = int(input().strip())
c = list(map(int, input().rstrip().split()))

i = 0
path = [0]
while i < n - 3:
    if c[i + 2] == 0:
        i += 2
    else:
        i += 1
    path.append(i)
path.append(n - 1)

print(f"{len(path) - 1}\n")
