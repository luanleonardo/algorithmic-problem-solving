from sys import stdin, stdout

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parametersu:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#


def matchingStrings(stringList, queries):
    query_counter = {query: 0 for query in queries}
    for string in stringList:
        if string not in query_counter:
            continue
        query_counter[string] += 1
    return [query_counter[query] for query in queries]


if __name__ == "__main__":

    stringList_count = int(stdin.readline().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = stdin.readline().strip()
        stringList.append(stringList_item)

    queries_count = int(stdin.readline().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = stdin.readline().strip()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    stdout.write("\n".join(map(str, res)))
    stdout.write("\n")
