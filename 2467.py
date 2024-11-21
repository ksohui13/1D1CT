#2467
#이분탐색

N = int(input())
liquids = [int(i) for i in input().split()]

s = 0 
e = N - 1

ans_r = 0
ans_l = 0

ans_sum = 2000000000 #(범위가 -1,000,000,000≤liquid≤1,000,000,000 이므로 최대 합)

while s < e:
    now_sum = liquids[s] + liquids[e]

    #합의 절댓값 확인 후 갱신
    if abs(now_sum) <= ans_sum:
        ans_l = liquids[s]
        ans_r = liquids[e]
        ans_sum = abs(now_sum)

    if now_sum <= 0:
        s += 1
    else:
        e -= 1

print(ans_l, ans_r)
    