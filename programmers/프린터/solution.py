from collections import deque

if __name__ == '__main__':
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    answer = 0

    target_number = priorities[location]
    index_arr = [0 for _ in range(len(priorities))]
    index_arr[location] = 1

    deque = deque(priorities)
    while deque:
        max_value = max(deque)

        temp = deque.popleft()
        temp_index = index_arr.pop(0)

        if temp < max_value:
            deque.append(temp)
            index_arr.append(temp_index)
        else:
            answer += 1

            if temp_index == 1:
                break

    print(answer)

