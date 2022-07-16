if __name__ == "__main__":
    h, w = map(int, input().split())
    arr = list(map(int, input().split()))

    max_height = 1
    max_index = 0
    for index, value in enumerate(arr):
        if value > max_height:
            max_height = value
            max_index = index

    total = 0
    value = 0
    for i in range(max_index + 1):
        # 최대 전까지 반복
        if arr[i] > value:
            value = arr[i]
        total += value

    value = 0
    for i in range(w-1, max_index, -1):
        # 최대 이후부터 끝까지 반복
        if arr[i] > value:
            value = arr[i]
        total += value

    print(total - sum(arr))