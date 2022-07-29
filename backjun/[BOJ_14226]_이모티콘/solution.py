from collections import deque


def bfs(screen, clip, count):
    global target
    d = deque()
    d.append((screen, clip, count))
    visited[screen][clip] = True

    while d:
        temp_screen, temp_clip, temp_count = d.popleft()

        if temp_screen == target:
            return temp_count

        # 클립보드에 넣기 temp_clip = temp_screen
        if not visited[temp_screen][temp_screen]:
            visited[temp_screen][temp_screen] = True
            d.append((temp_screen, temp_screen, temp_count + 1))

        # 클립보드 붙여넣기
        if not visited[temp_screen + temp_clip][temp_clip] and 1 <= temp_screen + temp_clip <= target:
            visited[temp_screen + temp_clip][temp_clip] = True
            d.append((temp_screen + temp_clip, temp_clip, temp_count + 1))

        # 1개 삭제
        if not visited[temp_screen - 1][temp_clip] and 1 <= temp_screen - 1 <= target:
            visited[temp_screen - 1][temp_clip] = True
            d.append((temp_screen - 1, temp_clip, temp_count + 1))


if __name__ == '__main__':
    target = int(input())
    visited = [[False] * 2001 for _ in range(2001)]

    print(bfs(1, 0, 0))  # 현재, 클립보드, 카운트
