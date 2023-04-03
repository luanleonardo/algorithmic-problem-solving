# https://www.algoexpert.io/questions/sorted-squared-array


# O(N) time | O(N) space, N = z length
def _split(z):
    x = []
    y = []
    for n in z:
        if n < 0:
            x.append(n * n)
        else:
            y.append(n * n)
    x = x[::-1]
    return x, y


# O(N) time | O(N) space, N = x length + y length
def _merge(x, y):
    i = 0
    j = 0
    z = []
    while i < len(x) or j < len(y):
        if j == len(y) or i < len(x) and x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z


# O(N) time | O(N) space, N = z length
def sortedSquaredArray(z):
    x, y = _split(z)
    if len(x) > 0 and len(y) > 0:
        return _merge(x, y)
    return x + y


if __name__ == "__main__":
    array = [-7, -3, 1, 9, 22, 30]
    print(sortedSquaredArray(array))
