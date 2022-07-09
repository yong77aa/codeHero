# 프로그래머스 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def DFS(n):
    global answer

    visitied[n] = 1
    for i in range(len(computers)):
        if visitied[i] == 0 and computers[n][i]:
            # 방문할 수 있는 노드
            DFS(i)


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    visitied = [0] * n
    print(visitied)

    answer = 0
    for i in range(n):
        if visitied[i] == 0:
            DFS(i)
            answer += 1

    print(answer)


