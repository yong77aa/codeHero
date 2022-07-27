def dfs(v):
    global result

    visited[v] = True

    for i in range(1, n+1):
        if arr[v][i] == 1 and not visited[i]:
            result += 1
            dfs(i)


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    arr = [[0] * (n+1) for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    visited = [False] * (n+1)
    result = 0

    dfs(1)
    print(result)