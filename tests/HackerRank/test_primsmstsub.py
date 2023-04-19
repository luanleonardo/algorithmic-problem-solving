from HackerRank.primsmstsub import prims


def test_prim_heap_based_algo():
    """
    Test Case:
    5 6
    1 2 3
    1 3 4
    4 2 6
    5 2 2
    2 3 5
    3 5 7
    1
    """
    n, m = 5, 6
    edges = [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]]
    start = 1

    expected = 15
    min_cost, mst = prims(n=n, edges=edges, start=start)
    assert expected == min_cost
