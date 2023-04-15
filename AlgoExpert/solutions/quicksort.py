from random import randint


def choose_pivot(array, l, r):
    return randint(l, r)


def partition(array, l, r):
    p = array[l]
    i = l + 1
    # invariante do laço:
    # valores com índices [l + 1, i - 1] < p
    # valores com índices [i, j - 1] >= p
    for j in range(l + 1, r + 1):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[l], array[i - 1] = array[i - 1], array[l]
    return i - 1


def quicksort(array, l, r):
    # caso base
    if l >= r:
        return

    # escolhe índice do pivot
    i = choose_pivot(array, l, r)

    # troca pivot com valor na posição l
    array[l], array[i] = array[i], array[l]

    # particiona array em torno do pivot
    j = partition(array, l, r)

    # valores com índices [l, j - 1]  < pivot
    # valores com índices [j + 1, r] >= pivot
    quicksort(array, l, j - 1)
    quicksort(array, j + 1, r)


if __name__ == "__main__":
    array = [5, 5, 2, 9, 8, 6, 3]
    quicksort(array, l=0, r=len(array) - 1)
    print(array)
