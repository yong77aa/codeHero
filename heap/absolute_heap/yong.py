# 백준알고리즘 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq

n = int(sys.stdin.readline())
my_head = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(my_head) == 0:
            # 배열이 비어있음
            print(0)
        else:
            # 비어있지 않으면
            print(heapq.heappop(my_head)[1])
    else:
        heapq.heappush(my_head, (abs(x), x))