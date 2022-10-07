# https://www.hackerrank.com/challenges/ctci-making-anagrams/

from collections import Counter
from sys import stdin, stdout

a = Counter(stdin.readline().rstrip())
b = Counter(stdin.readline().rstrip())

a_full_outer_join_b = (a - b) + (b - a)
stdout.write(f"{sum(a_full_outer_join_b.values())}\n")
