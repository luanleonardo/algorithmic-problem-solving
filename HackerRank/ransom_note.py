# https://www.hackerrank.com/challenges/ctci-ransom-note/

from collections import Counter

if __name__ == "__main__":
    m, n = map(int, input().rstrip().split())
    magazine = Counter(input().rstrip().split())
    note = Counter(input().rstrip().split())
    note_can_be_formed = all(
        word in magazine and note[word] <= magazine[word] for word in note
    )
    print(f"{'Yes' if note_can_be_formed else 'No'}")
