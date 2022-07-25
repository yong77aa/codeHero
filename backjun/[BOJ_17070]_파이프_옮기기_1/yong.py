def dfs(x, y, type):
    global answer, horizon, vertical, diagonal
    if (x, y) == (n-1, n-1):
        answer += 1
        return

    if type == vertical or type == diagonal:
        # 세로, 대각선 상태에서만 세로로 이동 가능
        if x+1 < n and arr[x+1][y] == 0:
            dfs(x+1, y, vertical)
    if type == horizon or type == diagonal:
        # 가로, 대각선 상태에서만 가로로 이동 가능
        if y+1 < n and arr[x][y+1] == 0:
            dfs(x, y+1, horizon)
    if x+1 < n and y+1 < n:
        # 마지막으로 모든 상태에서는 대각선으로 이동 가능
        if arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0:
            dfs(x+1, y+1, diagonal)


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    horizon = 0
    vertical = 1
    diagonal = 2

    dfs(1, 0, horizon)
    print(answer)
