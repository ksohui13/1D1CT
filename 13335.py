#13335
#구현/시뮬레이션

import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())

#트럭 무게
trucks = list(map(int, input().split()))

#다리 리스트
bridge = [0] * w

#시간 변수
time = 0

while bridge:
    time += 1 #시간 증가
    bridge.pop(0) #다리에 빈자리 생성

    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0)) #최대하중 이하일때 트럭 추가

        else:
            bridge.append(0) #최대 하중이 넘으면 다리 위에서 제거한다

print(time)
