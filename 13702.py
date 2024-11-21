#13702
#이분탐색

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

pots = [int(input()) for _ in range(N)]

s = 1
e = max(pots)

answer = 0

while s <= e:
    mid = (s + e) // 2

    person = 0
    for pot in pots:
        person += pot // mid

    if person >= K:
        answer = mid
        s = mid + 1

    else:
        e = mid - 1

print(answer)