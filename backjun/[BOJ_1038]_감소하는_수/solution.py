import sys
sys.stdin = open("input.txt", "r")


def isDown(target):
    global count, temp
    arr = []
    for i in str(target):
        arr.append(i)

    if len(arr) == 1:
        count += 1
        return
    else:
        for i in range(len(arr)-1, -1, -1):
            if i != 0:
                if arr[i-1] <= arr[i]:
                    return
    count += 1


if __name__ == "__main__":
    n = int(input())
    count = 0
    temp = 0

    while True:
        if count == n:
            print(temp)
            break
        else:
            temp += 1
            isDown(temp)
