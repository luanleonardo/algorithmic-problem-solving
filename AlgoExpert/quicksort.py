from random import randint


def choose_pivot(array, left, right):
    return randint(left, right)


def partition(array, left, right):
    p = array[left]
    i = left + 1
    # invariante do laço:
    # valores com índices [l + 1, i - 1] < p
    # valores com índices [i, j - 1] >= p
    for j in range(left + 1, right + 1):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1


def quicksort(array, left, right):
    # caso base
    if left >= right:
        return

    # escolhe índice do pivot
    i = choose_pivot(array, left, right)

    # troca pivot com valor na posição l
    array[left], array[i] = array[i], array[left]

    # particiona array em torno do pivot
    j = partition(array, left, right)

    # valores com índices [l, j - 1]  < pivot
    # valores com índices [j + 1, r] >= pivot
    quicksort(array, left, j - 1)
    quicksort(array, j + 1, right)


if __name__ == "__main__":
    array = [5, 5, 2, 9, 8, 6, 3]
    quicksort(array, left=0, right=len(array) - 1)
    print(array)
