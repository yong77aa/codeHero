if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [0] * (n+1)

    for i in range(n-1, -1, -1):
        if i+1 <= n:
            # 해당 일에 일할지 안할지 비교
            dy[i] = max(dy[i], dy[i+1])
        if i + arr[i][0] <= n:
            # 근무기간 내에 일해야함
            waste_time = arr[i][0]  # 상담 소요기간
            money = arr[i][1]  # 받는 금액
            dy[i] = max(dy[i], money + dy[i + waste_time])

    print(max(dy))