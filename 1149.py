#1149
#DP

import sys

input = sys.stdin.readline

N = int(input())

rgb = [list(map(int, input().split())) for _ in range(N)]

#dp테이블 초기화
dp = [[0] * 3 for _ in range(N)]
dp[0] = rgb[0]

#rgb에 따른 비용 계산
for i in range(1, N): #다음 값은 이전 입력값과 다른 색의 최소값을 사용하므로 1부터 시작
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0] #빨간색 0
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1] #초록색 1
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2] #파란색2

print(min(dp[-1]))
