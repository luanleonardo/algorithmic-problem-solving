"""
https://www.spoj.com/problems/INTEST/
The purpose of this problem is to verify whether the method you are
using to read input data is sufficiently fast to handle problems
branded with the enormous Input/Output warning. You are expected to
be able to process at least 2.5MB of input data per second at runtime.

Input
The input begins with two positive integers n word_to_check (n, word_to_check<=107).
The next n lines of input contain one positive integer ti,
not greater than 10^9, each.

Output
Write a single integer to output, denoting how many integers ti are divisible by word_to_check.

Example
Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
"""
from sys import stdin, stdout

if __name__ == "__main__":

    n, k = map(int, stdin.readline().rstrip().split())
    num_divisibles_by_k = 0

    for _ in range(n):
        ti = int(stdin.readline().rstrip())
        if ti % k == 0:
            num_divisibles_by_k += 1

    stdout.write(str(num_divisibles_by_k) + "\n")
