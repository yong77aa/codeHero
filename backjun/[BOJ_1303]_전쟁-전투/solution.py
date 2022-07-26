def dfs(x, y, target):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < m and 0 <= ny < n:
            if not visited[nx][ny] and arr[nx][ny] == target:
                visited[nx][ny] = 1
                count += 1
                dfs(nx, ny, target)
    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(m)]
    w = b = 0

    visited = [[False] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            count = 1
            if not visited[i][j]:
                if arr[i][j] == 'W':
                    visited[i][j] = 1
                    dfs(i, j, 'W')
                    w += count ** 2
                elif arr[i][j] == 'B':
                    visited[i][j] = 1
                    dfs(i, j, 'B')
                    b += count ** 2

    print("%d %d" % (w, b))