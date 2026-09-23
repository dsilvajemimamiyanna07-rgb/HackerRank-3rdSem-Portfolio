import os

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    
    for q in queries:
        query_type, x, y = q[0], q[1], q[2]
        idx = (x ^ lastAnswer) % n
        
        if query_type == 1:
            arr[idx].append(y)
        elif query_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)
            
    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
        
    result = dynamicArray(n, queries)
    print('\n'.join(map(str, result)))