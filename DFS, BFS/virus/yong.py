# 백준알고리즘 바이러스
# https://www.acmicpc.net/problem/2606


def DFS(v):
    global result

    visited[v] = 1
    for i in range(1, n+1):
        if arr[v][i] == 1 and visited[i] == 0:
            # 방문할 수 있는 노드
            DFS(i)
            result += 1


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    arr = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    visited = [0] * (n+1)
    result = 0

    DFS(1)
    print(result)