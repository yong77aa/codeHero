import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(x, y):
    global count
    # 상, 하, 좌, 우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
                count += 1


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    apart_count = []
    count = 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
                apart_count.append(count)
                count = 1

    print(len(apart_count))
    apart_count.sort()
    for i in apart_count:
        print(i)