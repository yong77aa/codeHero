# 백준 괄호 뒤집기 문제
# https://www.acmicpc.net/problem/9093

if __name__ == '__main__':
    n = int(input())
    word_arr = []

    for i in range(n):
        word_arr.append(str(input()))

    for i in word_arr:
        split_word = i.split()
        for j in split_word:
            print(j[::-1], end=" ")
        print()