import pytest

from HackerRank.kruskalmstrsub import UnionFind, build_graph, kruskal


@pytest.fixture
def graph():
    """
    Build graph from test case 2: https://www.hackerrank.com/challenges/kruskalmstrsub/problem?isFullScreen=false#!
    5 7
    1 2 20
    1 3 50
    1 4 70
    1 5 90
    2 3 30
    3 4 40
    4 5 60
    """
    edges = [
        [1, 2, 20],
        [1, 3, 50],
        [1, 4, 70],
        [1, 5, 90],
        [2, 3, 30],
        [3, 4, 40],
        [4, 5, 60],
    ]
    return build_graph(edges)


def test_union_find():
    n = 5
    uf = UnionFind(n)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(1, 3)
    assert uf.find(1) == uf.find(2)
    assert uf.find(2) == uf.find(3)
    assert uf.find(1) == uf.find(3)


def test_kruskal_mst_algo(graph):
    expected = 150
    min_cost, mst = kruskal(graph=graph)
    assert expected == min_cost
