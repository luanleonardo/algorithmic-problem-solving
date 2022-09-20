from sys import stdin, stdout


if __name__ == "__main__":

    SET = int(stdin.readline().rstrip())
    for _ in range(SET):

        N, S, Q = map(int, stdin.readline().rstrip().split())
        cargo_station = list()
        for i in range(N):

            line_i = list(map(int, stdin.readline().rstrip().split()))
            cargo_station.append(line_i[1:])

        cargo_carrier = list()
        time_spent = 0
        while cargo_carrier or any(station != [] for station in cargo_station):

            for i in range(N):
                # try to unload the carrier
                while cargo_carrier:

                    if cargo_carrier[-1] - 1 == i:
                        time_spent += 1
                        cargo_carrier.pop()
                    elif len(cargo_station[i]) < Q:
                        time_spent += 1
                        cargo_station[i].append(cargo_carrier.pop())
                    else:
                        break
                # try to load the carrier
                while len(cargo_carrier) < S and cargo_station[i]:

                    time_spent += 1
                    cargo_carrier.append(cargo_station[i].pop(0))

                if cargo_carrier or any(station != [] for station in cargo_station):
                    time_spent += 2
                else:
                    break

        stdout.write(f"{time_spent}\n")
