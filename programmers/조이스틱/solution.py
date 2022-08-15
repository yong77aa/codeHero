if __name__ == "__main__":
    name = "AAAABABAAAA"
    answer = 0

    up_down = 0
    left_right = len(name) - 1

    for index, value in enumerate(name):
        up_down += min(ord(value) - ord('A'), ord('Z') - ord(value) + 1)

        next = index + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        left_right = min([left_right, 2 * index + len(name) - next, index + 2 * (len(name) - next)])

    answer = up_down + left_right
    print(answer)