from sys import stdin, stdout


if __name__ == "__main__":

    c = int(stdin.readline().rstrip())
    for _ in range(c):

        l, m = map(int, stdin.readline().rstrip().split())
        river_bank = {"left": [], "right": []}

        for i in range(m):

            line_i = stdin.readline().rstrip().split()
            river_bank[line_i[1]].append(int(line_i[0]))

        ferry = {"size": l * 100, "deck": []}
        times_ferry_crosses_river = 0

        while ferry["deck"] or river_bank["left"] or river_bank["right"]:

            for bank in river_bank:

                ferry["deck"] = []
                while river_bank[bank]:

                    if sum(ferry["deck"]) + river_bank[bank][0] <= ferry["size"]:
                        ferry["deck"].append(river_bank[bank].pop(0))
                    else:
                        break

                if ferry["deck"] or river_bank["left"] or river_bank["right"]:
                    times_ferry_crosses_river += 1
                else:
                    break

        stdout.write(f"{times_ferry_crosses_river}\n")
