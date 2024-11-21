# #4963
# #bfs

import sys
from collections import deque

input = sys.stdin.readline


# BFS 함수
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1 #방문 처리

    while queue:
        x, y = queue.popleft()

        # 이동 #이동할 수 있는 방향은 8방향 (상, 하, 좌, 우, 북동, 북서, 남동, 남서)
        for i in range(8):
            dx, dy = x + directions[i][0], y + directions[i][1]

            # 이동 위치가 범위 내이고 방문하지 않았으며 땅이라면 탐색 지속
            if 0 <= dx < h and 0 <= dy < w and not visited[dx][dy] and graph[dx][dy]:
                queue.append((dx, dy))
                visited[dx][dy] = 1


# 이동할 수 있는 방향 8개
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

while True:
    w, h = map(int, input().split())

    # 입력에 0, 0 들어올 때까지
    if w == 0 and h == 0:break

    else:
        # 지도 정보 받기
        graph = [list(map(int, input().split())) for _ in range(h)]

        # 방문 리스트
        visited = [[0] * w for _ in range(h)]

        # 섬 개수
        count = 0

        # 전체 지도 탐색하기 - bfs
        for i in range(h):
            for j in range(w):
                # 섬을 찾았으며 방문한 섬이 아닐경우 bfs 수행
                if graph[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
                    count += 1 #gfs 이후 섬 개수 증가

        #섬 개수 출력
        print(count)