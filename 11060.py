#11060
#dp

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1001] * N #최댓값(미로 길이)으로 채워두기
dp[0] = 0 #초기화

for i in range(N):
    for j in range(1, A[i] + 1):
        if i + j < N: #범위에 적합한지 확인
            dp[i + j] = min(dp[i + j], dp[i] + 1)

#마지막 칸에 최소 점프 횟수가 갱신되지 않았을 경우 -1 출력
if dp[N-1] == 1001:
    print(-1)

#마지막칸에 최소 점프횟수 갱신시 갱신값 출력
else:
    print(dp[N-1])