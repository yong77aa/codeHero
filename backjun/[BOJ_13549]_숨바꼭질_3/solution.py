from collections import deque


def bfs(num):
    global k
    d = deque()
    d.append((num, 0))
    visited[num] = 1

    while d:
        temp, count = d.popleft()

        if temp == k:
            return count

        if 0 <= temp * 2 < 100001 and visited[temp * 2] == 0:
            visited[temp * 2] = 1
            d.append((temp * 2, count))

        if 0 <= temp - 1 < 100001 and visited[temp - 1] == 0:
            visited[temp - 1] = 1
            d.append((temp - 1, count + 1))

        if 0 <= temp + 1 < 100001 and visited[temp + 1] == 0:
            visited[temp + 1] = 1
            d.append((temp + 1, count + 1))


if __name__ == "__main__":
    n, k = map(int, input().split())
    visited = [0] * 100001

    print(bfs(n))