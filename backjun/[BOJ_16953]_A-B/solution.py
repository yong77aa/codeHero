from collections import deque


def bfs(k, count):
    q = deque()
    q.append((k, count))

    while q:
        x, y = q.popleft()
        if x > b:
            continue
        if x == b:
            print(y)
            break
        q.append((int(str(x) + "1"), y + 1))
        q.append((x * 2, y + 1))
    else:
        print(-1)


def dfs(k, count):
    global Min

    if k > b:
        return

    if k == b:
        Min = count
        return

    dfs(k * 2, count + 1)
    dfs(int(str(k) + "1"), count + 1)


if __name__ == "__main__":
    a, b = map(int, input().split())
    Min = -1

    dfs(a, 1)

    print(Min)
