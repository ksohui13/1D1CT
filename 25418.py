#25418

import sys
input = sys.stdin.readline

A, K = map(int, input().split())
count = 0

while True:
    if A == K:
        break

    else:
        if K % 2 == 0 and K//2 >= A:
            K//=2
            count+= 1

        else:
            K-=1
            count += 1

print(count)