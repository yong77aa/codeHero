def dfs(x, y):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and arr[nx][ny] == '#':
                visited[nx][ny] = True
                count += 1
                dfs(nx, ny)
    return


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        arr[a-1][b-1] = '#'

    visited = [[False] * m for _ in range(n)]
    result = 0
    count = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == '#':
                visited[i][j] = True
                dfs(i, j)
                result = max(result, count)
                count = 1

    print(result)