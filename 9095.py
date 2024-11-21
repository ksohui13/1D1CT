#9095
#DP

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input()) #정수 입력받기

    #dp 테이블
    dp = [0] * 12

    #점화식 초기화
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    #4이상의 n의 값에 대한 계산
    for i in range(4, 11): #4부터 10까지
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])