# 백준알고리즘 중앙값 구하기
# https://www.acmicpc.net/problem/2696

n = int(input())

for i in range(n):
    m = int(input())
    arr = []
    if m > 10:
        for i in range(int(m/10)+1):
            arr += list(map(int, input().split()))
    else:
        arr = list(map(int, input().split()))

    median_arr = []
    for j in range(1, m+1, 2):
        median = round((j-1)/2) + 1
        temp_arr = arr[:j]
        temp_arr.sort()
        median_arr.append(temp_arr[median-1])

    print(len(median_arr))
    count = 0

    if len(median_arr) > 10:
        for i in median_arr:
            print(i, end=' ')
            count += 1

            if count == 10:
                print("")
                count = 0
    else:
        print(*median_arr)
