# https://www.hackerrank.com/challenges/special-palindrome-again/

from sys import stdin, stdout


def pad(s):
    return "!".join(s)


def unpad(s):
    return s.replace("!", "")


def get_special_palindromic_substrings(s):
    s = pad(s)
    palindromes = []
    for center in range(len(s)):
        left, right = center, center
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome = unpad(s[left : right + 1])
            if s[left] != "!" and len(set(palindrome)) <= 2:
                palindromes.append(palindrome)
            left -= 1
            right += 1
    return palindromes


n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
stdout.write(f"{len(get_special_palindromic_substrings(s))}\n")
