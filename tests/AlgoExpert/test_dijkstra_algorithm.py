import pytest

from AlgoExpert.dijkstra_algorithm import (
    build_directed_graph,
    dijkstra,
    dijkstrasAlgorithm,
)


@pytest.fixture
def start():
    return 0


@pytest.fixture
def edges():
    return [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]


@pytest.fixture
def expected_graph():
    return {
        0: {1: 7},
        1: {2: 6, 3: 20, 4: 3},
        2: {3: 14},
        3: {4: 2},
        4: {},
        5: {},
    }


@pytest.fixture
def expected_distances():
    return [0, 7, 13, 27, 10, float("inf")]


@pytest.fixture
def expected_result():
    return [0, 7, 13, 27, 10, -1]


def test_build_graph(edges, expected_graph):
    result_graph = build_directed_graph(edges=edges)
    assert expected_graph == result_graph


def test_dijkstra(expected_graph, start, expected_distances):
    result_distances = dijkstra(graph=expected_graph, start=start)
    assert expected_distances == result_distances


def test_dijkstrasAlgorithm(start, edges, expected_result):
    result = dijkstrasAlgorithm(start, edges)
    assert expected_result == result
