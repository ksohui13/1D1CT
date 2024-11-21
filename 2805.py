#2805
#이분탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

#이분탐색 범위
s = 0
e = max(trees)

#이분 탐색
while s <= e:
    mid = (s + e) // 2
    cuts = 0 #잘린 길이 합

    for tree in trees:
        if tree > mid: #절단기 높이보다 높은 나무만 자르기
            cuts += tree - mid

    # 잘린 나무길이의 합이 M 이상이면
    if cuts >= M:
        s = mid + 1 #중앙값 + 1

    # 잘린 나무 길이의 합이 M보다 작으면
    else:
        e = mid - 1 #중앙값 - 1

print(e)