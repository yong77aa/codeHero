# 백준알고리즘 N번째 큰 수
# https://www.acmicpc.net/problem/2693

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        print(arr[2])