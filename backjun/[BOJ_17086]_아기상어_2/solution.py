from collections import deque


def bfs():
    global result
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    while d:
        temp_a, temp_b = d.popleft()

        for i in range(8):
            nx = temp_a + dx[i]
            ny = temp_b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                d.append((nx, ny))
                board[nx][ny] = board[temp_a][temp_b] + 1
                result = max(result, board[nx][ny])


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    d = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                d.append((i, j))

    result = 0
    bfs()

    print(result-1)