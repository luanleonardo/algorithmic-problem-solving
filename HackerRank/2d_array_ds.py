from sys import stdin, stdout

arr = []
for _ in range(6):
    arr.append(list(map(int, stdin.readline().rstrip().split(" "))))

highest_sum = float("-inf")
for i in range(1, 5):
    for j in range(1, 5):
        hourglass_sum = sum(
            [
                arr[r][c]
                for r, c in [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ]
            ]
        )
        if hourglass_sum > highest_sum:
            highest_sum = hourglass_sum

stdout.write(f"{highest_sum}\n")
