from collections import deque
import sys


input = sys.stdin.readline
n = int(input().strip())

graph = [list(map(int,list(input().strip()))) for _ in range(n)]
visit = [[False] * n for _ in range(n)] 
result = []


def bfs(y,x):
    if visit[y][x]:
        return
    queue = deque([(y,x)])
    visit[y][x] = True
    count = 1
    while queue:
        curr_y, curr_x = queue.popleft()
        # print(queue)

        for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny, nx = curr_y + dy, curr_x + dx
            if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx] and graph[ny][nx] == 1:
                visit[ny][nx] = True
                queue.append((ny,nx))
                count +=1


    result.append(count)


for y in range(n):
    for x in range(n):
        if not visit[y][x] and graph[y][x] == 1:
            bfs(y,x)

result.sort()
print(len(result))
for i in range(len(result)):   
    print(result[i])