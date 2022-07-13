# 백준알고리즘 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

if __name__ == '__main__':
    arr = []
    for i in range(9):
        temp = int(input())
        arr.append(temp)

    total = sum(arr)
    target = total-100

    a, b = 0, 0

    for i in range(9):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == target:
               a = arr[i]
               b = arr[j]

    arr.remove(a)
    arr.remove(b)
    arr.sort()

    for i in arr:
        print(i)
