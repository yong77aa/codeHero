from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    d = deque()
    d.append([x, y])

    while d:
        x, y = d.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                d.append([nx, ny])

    return maps[len(maps)-1][len(maps[0])-1]


if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

    print(bfs(0, 0))