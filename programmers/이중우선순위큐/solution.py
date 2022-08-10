import heapq

if __name__ == "__main__":
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    answer = []

    heap = []
    for i in operations:
        order, num = i.split(" ")
        num = int(num)
        if order == 'I':
            # 값 넣기
            heapq.heappush(heap, num)
        elif order == 'D':
            if not len(heap) == 0:
                if num == -1:
                    # 최소값
                    heapq.heappop(heap)
                elif num == 1:
                    # 최대값
                    heap.sort()
                    del heap[-1]

    if len(heap) == 0:
        answer = [0, 0]
    else:
        heap.sort()
        answer.append(heap[-1])
        answer.append(heap[0])

    print(answer)