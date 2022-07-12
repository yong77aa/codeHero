# 프로그래머스 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets):
    answer = []
    routes = dict()

    for (start, end) in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]

    for key in routes.keys():
        routes[key].sort(reverse=True)

    start = ["ICN"]

    while start:
        temp = start[-1]
        print("routes[temp]: " + str(routes[temp]))

        if not routes[temp]:
            # routes[temp]의 값이 False이면 실행
            # routes[temp]가 비어있으면 실행한다는 말임
            # False일 조건은? 빈 목록, 빈 사전, 빈 문자열, 빈 튜플, 빈 세트, Noen 개체
            # 더 갈게 없는 경우가 되는거임
            answer.append(start.pop())
        else:
            # 더 갈게 있는 경우
            start.append(routes[temp].pop())

    answer.reverse()
    return answer


if __name__ == '__main__':
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))


