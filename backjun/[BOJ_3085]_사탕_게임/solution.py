import sys
sys.stdin = open("input.txt", "r")


def check_max(x, y, target):
    max_val_x = 0
    max_val_y = 0

    for i in range(n):
        if arr[x][i] == target:
            max_val_x += 1

    for i in range(n):
        if arr[i][y] == target:
            max_val_y += 1

    return max(max_val_x, max_val_y)


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    answer = -1e9

    for i in range(n):
        for j in range(n):
            if j+1 < n:
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

                temp_max = check_max(i, j, arr[i][j])

                if temp_max > answer:
                    answer = temp_max

                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            # 행 바꾸기
            if i + 1 < n:
                # 인점한 것과 바꾸기
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

                temp_max = check_max(i, j, arr[i][j])

                if temp_max > answer:
                    answer = temp_max

                # 바꿨던 것을 다시 원래대로 돌려놓기
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

    print(answer)


