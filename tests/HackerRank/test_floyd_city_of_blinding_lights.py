import pytest

from HackerRank.floyd_city_of_blinding_lights import (
    build_distance_matrix,
    floyd_warshall,
)


@pytest.fixture
def num_vertices():
    return 4


@pytest.fixture
def weighted_edges():
    return [(0, 1, 5), (0, 3, 24), (1, 3, 6), (2, 3, 4), (2, 1, 7)]


def test_build_distance_matrix(num_vertices, weighted_edges):
    distance_matrix = build_distance_matrix(
        num_vertices=num_vertices, edges=weighted_edges
    )

    assert all(distance_matrix[u][u] == 0 for u in range(num_vertices))
    assert distance_matrix[0][1] == 5
    assert distance_matrix[0][2] == float("inf")
    assert distance_matrix[0][3] == 24


def test_floyd_warshall(num_vertices, weighted_edges):
    distance_matrix = build_distance_matrix(
        num_vertices=num_vertices, edges=weighted_edges
    )
    floyd_warshall(distance_matrix)

    assert distance_matrix[0][1] == 5
    assert distance_matrix[2][0] == float("inf")
    assert distance_matrix[0][3] == 11
