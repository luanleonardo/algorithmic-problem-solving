from AlgoExpert.task_assignment import taskAssignment


def test_assignment():
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    expected = [[0, 2], [4, 5], [1, 3]]
    actual = taskAssignment(k, tasks)

    assert expected == actual
