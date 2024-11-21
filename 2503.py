#2503
#구현/시뮬레이션

import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

#민혁이 숫자, 스트라이크, 볼
questions = [list(map(int, input().split())) for _ in range(N)]

#1~9까지 서로 다른 3개의 숫자를 고른 세 자리 수 생성
answers = list(permutations(range(1, 10), 3)) 

#답 개수
cnt = 0

for ans in answers:
    valid = True

    for quest in questions:
        quest_num = list(map(int, str(quest[0])))
        st, b = quest[1], quest[2]

        cnt_st, cnt_b = 0, 0

        for i in range(3):
            if ans[i] == quest_num[i]:
                cnt_st += 1
            elif ans[i] in quest_num:
                cnt_b += 1

        if cnt_st != st or cnt_b != b:
            valid = False
            break

    if valid:
        cnt += 1

print(cnt)
        