from collections import deque


def move_left(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2

def move_back_left(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    turned = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    deque = deque()
    deque.append([r, c, d])

    while deque:
        row, col, d = deque.popleft()
        temp_d = d

        for i in range(4):
            temp_d = move_left(temp_d)
            temp_r = row + dy[temp_d]
            temp_c = col + dx[temp_d]

            if 0 <= temp_r < n and 0 <= temp_c < m and board[temp_r][temp_c] == 0:
                answer += 1
                board[temp_r][temp_c] = 2
                deque.append([temp_r, temp_c, temp_d])
                break
            elif i == 3:
                temp_r, temp_c = row + dy[move_back_left(d)], col + dx[move_back_left(d)]
                deque.append([temp_r, temp_c, d])

                if board[temp_r][temp_c] == 1:
                    break

    print(answer)