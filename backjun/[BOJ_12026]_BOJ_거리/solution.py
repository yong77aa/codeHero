if __name__ == "__main__":
    n = int(input())
    arr = list(map(str, input()))
    next_step = {'B': 'O', 'O': 'J', 'J': 'B'}
    dp = [1e9] * n

    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] == next_step[arr[j]]:
                dp[i] = min(dp[i], dp[j] + pow(i-j, 2))

    if dp[n-1] == 1e9:
        print(-1)
    else:
        print(dp[n-1])