# https://www.algoexpert.io/questions/task-assignment


# O(n log n) time | O(n) space
def taskAssignment(k, tasks):
    sorted_tasks = sorted((v, i) for i, v in enumerate(tasks))
    return [
        [t1[1], t2[1]]
        for t1, t2 in zip(sorted_tasks[:k], sorted_tasks[k:][::-1])
    ]
