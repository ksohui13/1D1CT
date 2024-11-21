#13567
#구현

import sys

input = sys.stdin.readline

M, n = map(int, input().split())

#명령어
commands = [input().split() for _ in range(n)]

# 방향 : 동북서남
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 초기 방향 및 초기 위치
dir = 0
loc = [0, 0]

# 이동이 유효한가
valid = True

# for문을 통한 명령어 수행
for com in commands:
    # TURN
    if com[0] == 'TURN':
        if com[1] == '0': # 왼쪽 90도 회전
            dir = (dir + 1) % 4
        else: # 오른쪽 90도 회전
            dir = (dir - 1) % 4

    # MOVE
    else:
        loc[0] += directions[dir][0] * int(com[1])
        loc[1] += directions[dir][1] * int(com[1])

        if loc[0] < 0 or loc[0] > M or loc[1] < 0 or loc[1] > M:
            valid = False
            break

if not valid:
    print(-1)
else:
    print(' '.join(map(str, loc)))