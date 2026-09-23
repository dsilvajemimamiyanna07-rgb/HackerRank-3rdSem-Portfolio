def matchingStrings(stringList, queries):
    frequency = {}

    for string in stringList:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1

    result = []

    for query in queries:
        result.append(frequency.get(query, 0))

    return result


if __name__ == '__main__':
    n = int(input())

    stringList = []
    for _ in range(n):
        stringList.append(input().strip())

    q = int(input())

    queries = []
    for _ in range(q):
        queries.append(input().strip())

    result = matchingStrings(stringList, queries)

    for value in result:
        print(value)
