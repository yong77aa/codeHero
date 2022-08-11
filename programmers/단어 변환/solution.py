from collections import deque

def bfs(begin, target):
    d = deque()
    d.append([begin, 0])

    while d:
        word, count = d.popleft()
        if word == target:
            return count

        for i in range(len(words)):
            diff_count = 0
            for a, b in zip(word, words[i]):
                if a != b:
                    diff_count += 1

            if diff_count == 1:
                d.append([words[i], count + 1])


if __name__ == "__main__":
    answer = 0
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(bfs(begin, target))