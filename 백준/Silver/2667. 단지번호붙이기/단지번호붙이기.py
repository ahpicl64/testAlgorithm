from collections import deque
import queue
import sys


input = sys.stdin.readline
n = int(input())

graph = [list(map(int, list(input().strip()))) for _ in range(n)]
result = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visit = [[False] * n for _ in range(n)]

# 단지를 찾음
def bfs(x,y):
    queue = deque([(x,y)])
    if visit[y][x]:
        return
    # 단지 수 판정용 카운터
    visit[y][x] = True
    count = 1
    
    while queue: # 큐 다 빠질때까지
    # 이웃 노드 순회할 때 마다 카운트 + 1
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[ny][nx] and graph[ny][nx] == 1:
                visit[ny][nx] = True
                queue.append([nx,ny])
                count += 1

    # 카운트 된 집을 결과 리스트에 등록
    result.append(count)

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visit[y][x]:
            bfs(x,y)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])