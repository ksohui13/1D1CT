#14430
#DP

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#dp 테이블 정의
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + board[i-1][j-1] #max(한 칸 위, 한 칸 왼쪽) + 현재

print(dp[N][M])