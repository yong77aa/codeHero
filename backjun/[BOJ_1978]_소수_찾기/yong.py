# 백준알고리즘 소수 찾기
# https://www.acmicpc.net/problem/1978

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = []

    for i in arr:
        if i != 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                result.append(i)

    print(len(result))