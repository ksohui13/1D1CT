#2615
#구현/시뮬레이션

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

#방향 : 가로, 세로, 대각선 아래, 대각선 위 (우승 시 가장 왼쪽에 있는 좌표를 출력해야하므로)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]


for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            now = board[x][y]

            for i in range(4): #이동방향
                check = 1
                next_x = x + dx[i]
                next_y = y + dy[i]

                #현재 위치가 범위 내에 있으면서 위치가 일치할 때
                while 0 <= next_x < 19 and 0 <= next_y < 19 and board[next_x][next_y] == now:
                    check += 1

                    if check == 5:
                        #육목인지 체크
                        #첫번째 바둑돌보다 이전 바둑돌이 같은가
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x-dx[i]][y-dy[i]] == now:
                            break

                        #마지막 바둑돌 보다 앞의 바둑돌이 같은가
                        if 0 <= next_x + dx[i] < 19 and 0 <= next_y + dy[i] < 19 and board[next_x + dx[i]][next_y + dy[i]] == now:
                            break

                        #육목이 아닌 경우
                        print(now)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    next_x += dx[i]
                    next_y += dy[i]

print(0)