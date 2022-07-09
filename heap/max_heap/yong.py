# 백준알고리즘 최대 힙
# https://www.acmicpc.net/problem/11279

import sys
import heapq

n = int(input())
my_heap = []

for i in range(n):
    temp = int(sys.stdin.readline())

    if temp:
        heapq.heappush(my_heap, (-temp, temp))
    else:
        if len(my_heap) >= 1:
            print(heapq.heappop(my_heap)[1])
        else:
            print(0)

    