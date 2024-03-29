# https://www.algoexpert.io/questions/minimum-waiting-time


# O(n log n) time | O(1) space, n = number of queries
def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0
    num_queries = len(queries)
    for i, duration in enumerate(queries, start=1):
        waiting_time += duration * (num_queries - i)
    return waiting_time


if __name__ == "__main__":
    print(minimumWaitingTime(queries=[3, 2, 1, 2, 6]))
