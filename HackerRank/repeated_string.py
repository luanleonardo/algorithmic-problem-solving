s = input()
N = int(input().strip())

n = len(s)
q = N // n
r = N % n
num_as = sum([1 if c == "a" else 0 for c in s])

if r == 0:
    print(q * num_as)
else:
    num_as_remaining = sum([1 if c == "a" else 0 for c in s[:r]])
    print(q * num_as + num_as_remaining)
