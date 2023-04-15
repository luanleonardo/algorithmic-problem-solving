# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0

    f = max(0, array[0])
    if len(array) == 1:
        return f

    c = max(f, array[1])
    for v in array[2:]:
        f, c = c, max(c, f + max(0, v))
    return c
