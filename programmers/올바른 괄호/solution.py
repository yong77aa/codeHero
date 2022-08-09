from collections import deque

if __name__ == "__main__":
    s = "(()("
    answer = True

    deque = deque()
    for i in s:
        if i == '(':
            deque.append(i)
        else:
            if deque:
                deque.pop()

    if len(deque) != 0:
        answer = False
    else:
        answer = True

    print(answer)
