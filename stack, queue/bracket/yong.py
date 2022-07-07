# 백준 괄호 문제
# https://www.acmicpc.net/problem/9012

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        target = input()
        stack = []
        end_flag = False

        for i in target:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) != 0:
                    stack.pop()
                else:
                    print("NO")
                    end_flag = True
                    break

        if end_flag:
            continue
        else:
            if len(stack) != 0:
                print("NO")
            else:
                print("YES")
