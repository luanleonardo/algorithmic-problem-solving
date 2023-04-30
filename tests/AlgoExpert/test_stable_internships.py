from AlgoExpert.stable_internships import stableInternships


def test_stable_internship():
    interns = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 3, 1], [0, 2, 3, 1]]
    teams = [[1, 3, 2, 0], [0, 1, 2, 3], [1, 2, 3, 0], [3, 0, 2, 1]]
    expected = [[0, 1], [1, 0], [2, 2], [3, 3]]
    actual = stableInternships(interns, teams)

    assert sorted(actual) == expected
