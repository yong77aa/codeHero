from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])

    return arr[n-1][m-1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    answer = 0

    print(bfs(0, 0))
