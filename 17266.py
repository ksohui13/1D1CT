#17266
#구현

import sys
input = sys.stdin.readline


def bs(x, h):
    #첫번째 가로등
    if h - x[0] < 0 :
        return 0
    
    #사이 가로등
    for i in range(1, len(x) - 2):
        if(x[i] - x[i - 1]) / 2 > h:
            return 0
    
    #마지막 가로등      
    if N - x[-1] > h:
        return 0
    
    #모든 가로등 조건 만족
    return 1


N = int(input())
M = int(input())

x = list(map(int, input().split()))

start = 1
end = N

answer = 0

while start <= end:
    #중앙값
    middle = (start + end) // 2

    if bs(x, middle):
        end = middle - 1
        answer = middle

    else:
        start = middle + 1

print(answer)
