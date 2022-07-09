# 프로그래머스 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    answer = []

    for index, val in enumerate(prices):
        time = 0
        for j in range(index+1, len(prices)):
            print("i:%d j:%d" %(index, j))
            time += 1
            if val > prices[j]:
                # 가격이 떨어진 경우
                break
        answer.append(time)

print(answer)