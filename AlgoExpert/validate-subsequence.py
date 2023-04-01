# https://www.algoexpert.io/questions/validate-subsequence


# O(n) time | O(1) space, n  = array length
def isValidSubsequence(array, sequence):
    for e in sequence:
        try:
            i = array.index(e)
            array = array[i + 1:]
        except ValueError:
            return False
    return True


if __name__ == "__main__":
    print(
        isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, 10])
    )
