# 백준알고리즘 프린터
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

if __name__ == '__main__':
    priorities = list(map(int, input().split()))
    location = int(input())
    index_target = [0 for _ in range(len(priorities))]  # 목표 프린터의 위치를 저장하기 위한 배열
    index_target[location] = 1
    result = 0

    while priorities:
        max_value = max(priorities)

        # 첫번째를 뽑아서
        temp = priorities.pop(0)
        index = index_target.pop(0)

        if temp < max_value:
            # 우선순위가 가장 높지 않으면
            priorities.append(temp)  # 다시 맨 뒤로 넣음
            index_target.append(index)
        else:
            # 우선순위가 가장 높으면
            result += 1  # 프린트

            if index == 1:
                print(result)
                break

        # print(arr)
        # print(index_target)


