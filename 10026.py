#10026
#bfs

import sys
from collections import deque

input = sys.stdin.readline

#bfs
def bfs(x, y, color):
    queue = deque([(x, y)])
    visited[x][y] = 1 #방문처리
    now_color = grid[x][y] #현재 색깔

    while queue:
        x, y = queue.popleft()

        #구역 확인 - 상하좌우
        for i in range(4):
            dx, dy = x + directions[i][0], y + directions[i][1]

            #범위 내 이면서 방문하지 않은 색일경우 탐색
            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
                #적록색맹인 경우
                if color:
                    if now_color in 'RG' and grid[dx][dy] in 'RG': #RG 동일하게
                        queue.append((dx, dy)) #구역 추가
                        visited[dx][dy] = 1 #방문처리
                    elif now_color in 'B' and grid[dx][dy] in 'B': 
                        queue.append((dx, dy))
                        visited[dx][dy] = 1

                #적록색맹이 아닌 경우
                else:
                    if grid[dx][dy] == now_color:
                        queue.append((dx, dy))
                        visited[dx][dy] = 1

#필요한 입력 받기
N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]

#상하좌우
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#적록색맹인경우
visited = [[0] * N for _ in range(N)]
count_yes = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color = True)
            count_yes += 1 #bfs 탐색 한번에 구역 하나 찾으니까

#적록색맹이 아닌 경우
visited = [[0] * N for _ in range(N)]
count_no = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color=False)
            count_no += 1

print(count_no, count_yes)