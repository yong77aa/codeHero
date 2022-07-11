# 백준알고리즘 숨바꼭질
# https://www.acmicpc.net/problem/1697
from collections import deque


def BFS(n):
    q = deque([n])

    while q:
        v = q.popleft()
        if v == k:
            # 결과가 나온 경우
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


if __name__ == "__main__":
    n, k = map(int, input().split())
    visited = [0 for i in range(100001)]  # 방문 시간을 저장하기 위한 변수
    print(BFS(n))