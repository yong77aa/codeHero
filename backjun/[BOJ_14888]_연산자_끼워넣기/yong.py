def dfs(x, now):
    global n, plus, minus, multiple, divide, max_value, min_value

    if x == n:
        # 더 이상 연산할 수가 없는 경우
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        # 해당 연산자의 개수를 하나 줄이고
        # x의 값을 하나 증가시켜서 다음 숫자를 탐색하게 한 뒤, 연산한 뒤의 값을 넣음
        if plus:
            plus -= 1
            dfs(x+1, now + arr[x])
            plus += 1
        if minus:
            minus -= 1
            dfs(x+1, now - arr[x])
            minus += 1
        if multiple:
            multiple -= 1
            dfs(x+1, now * arr[x])
            multiple += 1
        if divide:
            divide -= 1
            if now < 0 and arr[x] > 0:
                # 음수
                abs_now = abs(now)
                dfs(x+1, -(abs_now // arr[x]))
            else:
                # 양수
                dfs(x+1, now // arr[x])
            divide += 1


if __name__ == "__main__":
    n = int(input())  # 숫자의 개수
    arr = list(map(int, input().split()))  # 수열
    plus, minus, multiple, divide = map(int, input().split())  # 덧셈, 뺄셈, 곱하기, 나누기

    # 최대, 최소값
    max_value = -1e49
    min_value = 1e49

    dfs(1, arr[0])  # 첫번째 인덱스 및 첫번째 수열의 값을 넣어서 재귀 시작
    print(max_value)
    print(min_value)