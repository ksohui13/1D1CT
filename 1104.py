#1326
#bfs

from collections import deque

n = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

def solution(a, b):
    q = deque([a]) # a번째 다리부터 탐색
    visited = [-1] * (n + 1)
    visited[a] = 0 #a번째 다리 시작점이므로 0으로 초기화

    #건너야 하는 다리 모두
    while q :
        now = q.popleft() #현재 건너는 다리

        #오른쪽
        for i in range(now, n + 1, bridge[now]):
            #탐색하지 않은 다리
            if visited[i] == -1:
                q.append(i) #건너야 하는 다리 추가
                visited[i] = visited[now] + 1 #점프 수

                #현재다리가 b라면
                if i == b:
                    return visited[i]
            
        #왼쪽
        for i in range(now, 0, -bridge[now]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1

                if i == b:
                    return visited[i]

    # 길을 찾지 못한 경우            
    return -1

print(solution(a, b))