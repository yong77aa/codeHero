import sys
sys.stdin = open("input.txt", "r")


def DFS(x, y):
    global n, count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if arr[x][y] == 1:
        count += 1
        arr[x][y] = 0
        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        return True


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    count = 0
    apart_count = []

    for i in range(n):
        for j in range(n):
            if DFS(i, j):
                apart_count.append(count)
                count = 0

    print(len(apart_count))
    apart_count.sort()
    for i in apart_count:
        print(i)