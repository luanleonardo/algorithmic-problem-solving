# https://www.algoexpert.io/questions/depth-first-search
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space, v = number of vertices, e = number of edges
    # def depthFirstSearch(self, array):
    #     explored = {id(self)}
    #     frontier = deque([self])
    #     while frontier:
    #         node = frontier.pop()
    #         array.append(node.name)
    #         for child in node.children[::-1]:
    #             if id(child) in explored:
    #                 continue
    #             explored.add(id(child))
    #             frontier.append(child)
    #     return array

    # O(v + e) time | O(v) space, v = number of vertices, e = number of edges
    # def depthFirstSearch(self, array, explored=None):
    #     if explored is None:
    #         explored = set()
    #     array.append(self.name)
    #     explored.add(id(self))
    #     for child in self.children:
    #         if id(child) in explored:
    #             continue
    #         child.depthFirstSearch(array, explored)
    #     return array

    # O(v + e) time | O(v) space, v = number of vertices, e = number of edges
    def depthFirstSearch(self, array):
        """DFS for a connected acyclic undirected graph."""
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
