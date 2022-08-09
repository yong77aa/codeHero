from collections import deque

if __name__ == "__main__":
    answer = 0
    jobs = [[0, 3], [1, 9], [2, 6]]
    jobs.sort(key=lambda x: x[1])

    task_arr = deque()
    length = len(jobs)
    i, start, now = 0, -1, 0
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                task_arr.append([job[1], job[0]])

        if task_arr:
            task_arr = sorted(task_arr, key=lambda x: x[0])
            task_arr = deque(task_arr)
            temp = task_arr.popleft()
            start = now
            now += temp[0]
            answer += now - temp[1]
            i += 1
        else:
            now += 1

    print(answer//length)