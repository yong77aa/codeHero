from collections import deque


def bfs(v, count):
    global k
    d = deque()
    d.append((v, count))
    visited[v] = True

    while d:
        temp, my_count = d.popleft()

        if temp == k:
            return my_count

        if not visited[temp * 2] and 0 <= temp * 2 <= 100000:
            visited[temp * 2] = True
            path[temp * 2] = temp
            d.append((temp * 2, my_count + 1))

        if not visited[temp + 1] and 0 <= temp + 1 <= 100000:
            visited[temp + 1] = True
            path[temp + 1] = temp
            d.append((temp + 1, my_count + 1))

        if not visited[temp - 1] and 0 <= temp - 1 <= 100000:
            visited[temp - 1] = True
            path[temp - 1] = temp
            d.append((temp - 1, my_count + 1))


def print_path(n, k):
    if n != k:
        print_path(n, path[k])
    print(k, end=' ')


if __name__ == '__main__':
    n, k = map(int, input().split())
    visited = [False] * 100001
    path = [0] * 100001

    print("result: %d" % (bfs(n, 0)))
    print_path(n, k)

    # result = []
    # temp_value = k
    #
    # for _ in range(k):
    #     result.append(temp_value)
    #     temp_value = path[temp_value]
    #
    # result.reverse()
    # print(*result)