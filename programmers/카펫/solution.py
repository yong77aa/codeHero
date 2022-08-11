if __name__ == '__main__':
    brown = 10
    yellow = 1
    answer = []
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    answer = [a, b]
                    break

    print(answer)