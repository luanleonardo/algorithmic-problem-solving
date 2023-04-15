from sys import stdin, stdout

if __name__ == "__main__":

    input_case_count = 0
    while True:

        input_case = stdin.readline().rstrip()
        if input_case == "end":
            break

        input_case_count += 1
        container_stacks = []
        for new_container in input_case:

            if (
                not container_stacks
                or new_container > container_stacks[-1][-1]
            ):
                container_stack = [new_container]
                container_stacks.append(container_stack)
                continue

            for container_stack in container_stacks:

                if new_container <= container_stack[-1]:
                    container_stack.append(new_container)
                    break

        stdout.write(
            f"Case {input_case_count}: {len(container_stacks)}" + "\n"
        )
