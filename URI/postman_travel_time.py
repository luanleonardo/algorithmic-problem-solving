from sys import stdin, stdout


def search_delivery_location(address_list, order):

    low_address = 0
    high_address = len(address_list) - 1

    while low_address <= high_address:

        mid_address = (low_address + high_address) // 2
        guess_address = address_list[mid_address]

        if guess_address == order:
            return mid_address
        elif guess_address > order:
            high_address = mid_address - 1
        else:
            low_address = mid_address + 1

    return None


if __name__ == "__main__":

    # Get the data
    N, M = map(int, stdin.readline().rstrip().split())
    addresses = list(map(int, stdin.readline().rstrip().split()))
    orders = list(map(int, stdin.readline().rstrip().split()))

    # Set the postman's starting position and start time
    postman_position = 0
    travel_time = 0

    # For each postman current_order, search for the delivery location,
    # calculate the travel time and update the postman's position.
    # The execution time of this loop has current_order O(M * log2(N))
    for current_order in orders:

        delivery_location = search_delivery_location(addresses, current_order)

        if postman_position != delivery_location:
            travel_time += abs(delivery_location - postman_position)
            postman_position = delivery_location

    # Shows the total travel time of the postman.
    stdout.write(f"{travel_time}" + "\n")
