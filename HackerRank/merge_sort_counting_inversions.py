from sys import stdin, stdout


def merge_and_count_split_inversions(C, D):

    n = len(C) + len(D)
    B = [0] * n
    i, j, split_invertions = 0, 0, 0

    for k in range(n):

        if i < len(C) and j < len(D):
            if C[i] <= D[j]:
                B[k] = C[i]
                i += 1
            else:
                B[k] = D[j]
                j += 1
                split_invertions += len(C) - i

        elif i < len(C) and j >= len(D):
            B[k] = C[i]
            i += 1

        elif i >= len(C) and j < len(D):
            B[k] = D[j]
            j += 1

    return B, split_invertions


def sort_and_count_inversions(A):

    n = len(A)
    if n == 0 or n == 1:
        return A, 0

    n_div_2 = n // 2
    C, left_invertions = sort_and_count_inversions(A[:n_div_2])
    D, right_invertions = sort_and_count_inversions(A[n_div_2:])
    B, split_invertions = merge_and_count_split_inversions(C, D)

    return B, left_invertions + right_invertions + split_invertions


if __name__ == "__main__":

    total_test_cases = int(stdin.readline().rstrip())

    for _ in range(total_test_cases):
        array_size = int(stdin.readline().rstrip())
        integer_array = list(map(int, stdin.readline().rstrip().split()))
        sorted_array, answer = sort_and_count_inversions(integer_array)
        stdout.write(f"{answer}\n")
