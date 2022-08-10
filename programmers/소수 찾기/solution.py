if __name__ == "__main__":
    numbers = int("17")
    answer = 0

    for i in range(2, numbers+1):
        for j in range(2, numbers):
            if i % j == 0:
                break
        else:
            # for문이 끝까지 돌아가면
            answer += 1

    print(answer)
