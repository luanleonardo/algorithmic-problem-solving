"""
https://www.hackerrank.com/challenges/no-prefix-set/problem
There is a given list of strings where each string contains only
lowercase letters from a-j, inclusive. The set of strings is said
to be a GOOD SET if no string is a prefix of another string.
In this case, print GOOD SET. Otherwise, print BAD SET on the first
line followed by the string being checked.

Note If two strings are identical, they are prefixes of each other.

Sample:
Input:
7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad

Output:
BAD SET
aabcde
"""
from sys import stdin, stdout


class TrieNode:
    def __init__(self, data):
        self.data = data
        self.is_end = False
        self.children = dict()


class Trie:
    """
    Implements a prefix tree with just the insert operation.
    Ref: https://en.wikipedia.org/wiki/Trie
    """

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                continue
            node = node.children[char]
        node.is_end = True


def is_a_good_set(trie, word):
    """
    The set of words (trie) is a good set if the parameter word
    is not prefix of any word in the set and no word in the
    set is prefix of the parameter word.
    """
    node = trie.root
    for char in word:
        if char not in node.children:
            return True
        node = node.children[char]
        if node.is_end:
            break
    return False


if __name__ == "__main__":

    result = "GOOD SET"
    word_set = Trie()
    number_of_words = int(stdin.readline().rstrip())
    for _ in range(number_of_words):

        word_to_check = stdin.readline().rstrip()
        if not is_a_good_set(word_set, word_to_check):
            result = "BAD SET"
            break
        word_set.insert(word_to_check)

    stdout.write(result + "\n")
    if result == "BAD SET":
        stdout.write(word_to_check + "\n")
