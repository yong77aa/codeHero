if __name__ == "__main__":
    n, s, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][s] = True

    for i in range(n):
        for j in range(m + 1):
            if not dp[i][j]:
                continue
            if j + v[i] <= m:
                dp[i + 1][j + v[i]] = True
            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = True

    answer = -1
    for i in range(m, -1, -1):
        if dp[n][i]:
            answer = i
            break

    print(answer)