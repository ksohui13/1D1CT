#1283
#구현

import sys
input = sys.stdin.readline


N = int(input())
sentence = [list(input().rstrip().split()) for _ in range(N)]

shortcuts = []

# for문을 통한 단축기 지정
for word in sentence:
    for i in range(len(word)):
        #첫글자가 단축키 아닐 때
        if word[i][0].lower() not in shortcuts:
            shortcuts.append(word[i][0].lower()) #단축키 추가
            word[i] = '[' + word[i][0] + ']' + word[i][1:] #단축키 출력 형식 : [단어]
            break

    # 첫글자 모두 있을 때
    else:
        for i in range(len(word)):
            # 첫 글자 이후의 문자부터 담색
            for j in range(1, len(word[i])):
                if word[i][j].lower() not in shortcuts: #단축키 아닐때
                    shortcuts.append(word[i][j].lower()) #단축키 지정
                    word[i] = word[i][:j] + '[' + word[i][j] + ']' + word[i][j + 1:] #단축키 출력 형식
                    break
            else:
                continue
            break

for word in sentence:
    print(' '.join(word))