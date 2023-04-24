from HackerRank.dijkstra_short_reach import dijkstra


def test_dijkstra():
    s = 1
    g = {0: {1: 10, 2: 6}, 1: {0: 10, 3: 8}, 2: {0: 6}, 3: {1: 8}, 4: {}}
    expected = [10, 0, 16, 8, float("inf")]
    result = dijkstra(graph=g, start=s)
    assert expected == result
