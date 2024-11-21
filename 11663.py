#11663
#이분 탐색

# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())

# dots = list(map(int, input().split()))

# for i in range(M):
#     start, end = map(int, input().split())
#     cnt = 0

#     for dot in dots:
#         if start <= dot <= end:
#             cnt += 1
#     print(cnt)


import sys
input = sys.stdin.readline

#선분의 시작점과 가까운 점의 위치 - 인덱스 번호로 접근
def min_dot(dots, target):
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2
        if dots[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

#선분의 마지막과 가까운 점의 위치
def max_dot(dots, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if dots[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

N, M = map(int, input().split())
dots = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(M)]

dots.sort()

for line in lines:
    start, end = line
    start_dot = min_dot(dots, start)
    end_dot = max_dot(dots, end)

    print(end_dot - start_dot)