from collections import deque


def bfs():
    global n, k
    min_time = -1
    min_time_count = 0

    d = deque()
    d.append((n, 0))

    if n == 0:
        d.append((n+1, 1))

    while d:
        temp, count = d.popleft()
        visited[temp] = True

        if temp == k:
            if min_time == -1:
                min_time = count

            elif min_time == count:
                min_time_count += 1
                continue

            else:
                break

        if 0 < temp <= 100000:
            if visited[temp-1] == 0:
                d.append((n-1, count+1))
            if visited[temp+1] == 0:
                d.append((n+1, count+1))
            if visited[temp*2] == 0:
                d.append((n*2, count+1))

    return min_time, min_time_count


if __name__ == "__main__":
    n, k = map(int, input().split())
    visited = [0] * 200001

    min_time, min_time_count = bfs()
    print(min_time)
