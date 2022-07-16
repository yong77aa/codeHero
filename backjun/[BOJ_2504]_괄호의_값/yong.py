from collections import deque


# 완벽한 괄호인지 체크
def my_check(t):
    left_stack = []

    for i in t:
        if i == '(' or i == '[':
            left_stack.append(i)
        elif left_stack[-1] == '(' and i == ')':
            left_stack.pop()
        elif left_stack[-1] == '[' and i == ']':
            left_stack.pop()

    if left_stack:
        return False
    return True


if __name__ == "__main__":
    target = input()

    if my_check(target):
        append_stack = []
        for i in target:
            if i == '(' or i == '[':
                append_stack.append(i)
            elif i == ')' or i == ']':
                # 닫는 기호
                temp = 2
                while True:
                    top = append_stack.pop()
                    if type(top) == int:
                        # 이미 계산된 값이 있는 경우
                        if i == ')':
                            temp = top * 2
                        elif i == ']':
                            temp = top * 3
                    elif top == '(' or top == '[':
                        # 또 여는 기호가 나온 경우
                        # 애초에 닫는 기호가 한번은 나온거니까 최초 값(2 or 3) 넣음
                        append_stack.append(temp)
                        break

            temp3 = 0
            while append_stack:
                top = append_stack.pop()
                if type(top) == int:
                    temp3 += top
                else:
                    append_stack.append(temp3)
                    break
    else:
        print(0)