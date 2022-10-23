# https://www.hackerrank.com/challenges/reverse-shuffle-merge

from collections import Counter, deque
from sys import stdin, stdout


def lexicographically_smallest_subsequence(s, k):
    n = len(s)
    ans = deque()
    for i, c in enumerate(s):
        while ans and c < ans[-1] and (len(ans) - 1 + n - i >= k):
            ans.pop()
        if not ans or len(ans) < k:
            ans.append(c)
    return "".join(ans)


def longest_anagram_subsequence(s1, s2):
    cs1 = Counter(s1)
    cs2 = Counter(s2)
    ans = 0
    for i in cs1:
        ans += min(cs1[i], cs2[i])
    return ans


if __name__ == "__main__":
    # s = stdin.readline().rstrip()
    s = 'abdecf'
    print(s, len(s))
    k = len(s) // 2
    s1, s2 = s[:k], s[k:]
    print(s1, s2)
    ans = longest_anagram_subsequence(s1, s2)
    print(ans)
