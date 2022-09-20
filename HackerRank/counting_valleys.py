from sys import stdin, stdout


def countingValleys(steps, path):
    on_the_mountain = False
    in_the_valley = False
    height = 0
    counter_valleys = 0

    for step in path:
        if step == "U":
            height += 1
        else:
            height -= 1

        if height > 0:
            in_the_valley = False
            on_the_mountain = True
        elif height < 0:
            in_the_valley = True
            on_the_mountain = False
        else:
            if in_the_valley:
                counter_valleys += 1
            in_the_valley = False
            on_the_mountain = False

    return counter_valleys


if __name__ == "__main__":

    steps = int(stdin.readline().strip())

    path = stdin.readline().strip()

    result = countingValleys(steps, path)

    stdout.write(str(result) + "\n")
