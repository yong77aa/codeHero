from collections import deque

if __name__ == "__main__":
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8
    answer = 0

    board = [[0] * 101 for i in range(101)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                board[i][j] = 1

    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                board[i][j] = 0

    visited = [[0] * 101 for i in range(101)]
    visited[characterX][characterY] = 1

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]

    d = deque([(characterX, characterY)])
    while d:
        x, y = d.popleft()

        if (x, y) == (itemX, itemY):
            answer = (board[x][y] - 1) // 2
            break

        for i in range(4):
            dx = x + mx[i]
            dy = y + my[i]

            if 0 <= dx < 101 and 0 <= dy < 101 and board[dx][dy] != 0 and visited[dx][dy] == 0:
                board[dx][dy] = board[x][y] + 1
                visited[dy][dy] = 1
                d.append((dx, dy))

