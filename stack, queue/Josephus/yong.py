# 백준 요세푸스 문제
# https://www.acmicpc.net/problem/1158

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [1 * (i+1) for i in range(n)]
    result = []

    while arr:
        if len(arr) < k:
            break

        temp = arr.pop(k-1)
        result.append(temp)

        after_arr = arr[k-1::]
        before_arr = arr[:k-1:]
        new_arr = after_arr + before_arr
        arr = new_arr

result = result + arr

for index, value in enumerate(result):
    if index == 0:
        print("<%d," %value, end=' ')
    elif index == len(result)-1:
        print("%d>" %value, end=' ')
    else:
        print("%d," %value, end=' ')