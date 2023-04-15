from sys import stdin, stdout

if __name__ == "__main__":

    while True:

        N, K = map(int, stdin.readline().rstrip().split())
        if N == 0 and K == 0:
            break

        parking_lot = []
        everyone_can_park = True
        for _ in range(N):

            arrival_time, departure_time = map(
                int, stdin.readline().rstrip().split()
            )
            if not parking_lot:
                parking_lot.append((arrival_time, departure_time))
                continue

            _, departure_time_top = parking_lot[-1]
            while arrival_time >= departure_time_top:

                parking_lot.pop()
                if not parking_lot:
                    break
                _, departure_time_top = parking_lot[-1]

            if not parking_lot or (
                departure_time < departure_time_top and len(parking_lot) < K
            ):
                parking_lot.append((arrival_time, departure_time))
                continue

            everyone_can_park = False

        stdout.write("Sim" + "\n") if everyone_can_park else stdout.write(
            "Nao" + "\n"
        )
