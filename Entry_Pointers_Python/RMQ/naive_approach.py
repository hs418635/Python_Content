def naive_rmq(arr, queries):

    results = []
    for L, R in queries:
        min_value = min(arr[L:R+1])
        results.append(min_value)

    return results

if __name__ == "__main__":
    arr = [2, 5, 1, 4, 9, 3]
    queries = [(1, 4), (2, 5), (0, 3)]
    print("Arrray:", arr)
    print("Queries:", queries)

    result = naive_rmq(arr, queries)
    print("Query results:", result)