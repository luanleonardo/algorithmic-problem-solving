import pytest

from AlgoExpert.solutions.depth_first_search import Node


@pytest.fixture
def graph_tree():
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    return graph


def test_dfs(graph_tree):
    actual = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
    expected = graph_tree.depthFirstSearch([])
    assert actual == expected
