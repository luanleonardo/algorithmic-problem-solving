# https://www.hackerrank.com/challenges/contacts

from sys import stdin, stdout


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = dict()


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1


def find(trie, word):
    node = trie.root
    for char in word:
        if char not in node.children:
            return 0
        node = node.children[char]
    return node.count


def contacts(queries):
    T = Trie()
    result = []
    for q, w in queries:
        if q == "add":
            T.add(w)
        else:
            result.append(find(T, w))
    return result


if __name__ == "__main__":

    n = int(stdin.readline().strip())
    queries = [stdin.readline().strip().split() for _ in range(n)]
    stdout.write("\n".join(map(str, contacts(queries))))
    stdout.write("\n")
