#27737
#BFS

import sys, math
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    farm[x][y] = 1 #방문처리
    areas = 1 #연결된 영역(최소 1개임)

    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 확인하기
        for i in range(4): #이동가능방향 4개(상하좌우)
            dx, dy = x + directions[i][0], y + directions[i][1]
            # 영역 내에 / 버섯이 자랄 수 있는 카닝 있는지 확인하기
            if 0 <= dx < N and 0 <= dy < N and farm[dx][dy] == 0:
                farm[dx][dy] = 1 #방문처리
                queue.append((dx, dy))
                areas += 1 #영역 카운트
    return areas


# N, M, K
N, M, K = map(int, input().split())

#나무판
farm = [list(map(int, input().split())) for _ in range(N)]

# 이동방향 - 상하좌우
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 필요한 버섯 포자 개수 
need_seed = 0

#최소 1개의 포자를 사용했는가
use_seed = False

# 전체 탐색하기
for i in range(N):
    for j in range(N):
        if farm[i][j] == 0:
            areas = bfs(i, j)
            left_seed = math.ceil(areas / K) #남은 포자 개수
            need_seed += left_seed #필요한 포자
            use_seed = True #포자를 사용했는가

if not use_seed:
    print('IMPOSSIBLE')
elif need_seed <= M:
    print('POSSIBLE')
    print(M - need_seed)
else:
    print('IMPOSSIBLE')