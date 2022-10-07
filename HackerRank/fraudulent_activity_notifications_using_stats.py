# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/
# https://thirdspacelearning.com/gcse-maths/statistics/median-from-a-frequency-table/

from sys import stdin, stdout


def get_median(frequency_table, d):

    even_number_of_values = d % 2 == 0
    position_of_the_median = d // 2
    middle_value_1, middle_value_2 = 0, 0

    cumulative_frequency = 0
    for expenditure, frequency in enumerate(frequency_table):
        cumulative_frequency += frequency

        if cumulative_frequency >= position_of_the_median and middle_value_1 == 0:
            middle_value_1 = expenditure

        if cumulative_frequency >= position_of_the_median + 1 and middle_value_2 == 0:
            middle_value_2 = expenditure
            break

    if even_number_of_values:
        return (middle_value_1 + middle_value_2) / 2

    return middle_value_2


if __name__ == "__main__":

    n, d = map(int, stdin.readline().strip().split())
    expenditures = list(map(int, stdin.readline().strip().split()))

    frequency_expenditures = [0] * 201
    for expenditure in expenditures[:d]:
        frequency_expenditures[expenditure] += 1

    notifications = 0
    for i in range(d, n):
        if expenditures[i] >= 2 * get_median(frequency_expenditures, d):
            notifications += 1
        frequency_expenditures[expenditures[i]] += 1
        frequency_expenditures[expenditures[i - d]] -= 1

    stdout.write(f"{notifications}\n")
