# 프로그래머스 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165#


def DFS(index, value, numbers, target):
    global answer

    n = len(numbers)
    if index == n and value == target:
        # 결과 값이 같은 경우
        return 1
    if index == n:
        # 끝까지 돌았지만 값이 다름
        return

    DFS(index + 1, value + numbers[index], numbers, target)
    DFS(index + 1, value - numbers[index], numbers, target)


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3

    answer = 0
    DFS(0, 0, numbers, target)