from collections import deque
m,n = map(int,input().split())

graph = [list(map(int,list(input().split()))) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
index_arr = []
zerocounter = 0
def bfs():
    global zerocounter
    queue = deque()
    if find_1(graph) == 'notomato':
        return print(0)
    for i in range(len(index_arr)):
        y, x = index_arr[i]
        visit[y][x] = True
        queue.append((y,x,-1))
    while queue:
        y, x, day = queue.popleft()
        day += 1
        for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny,nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visit[ny][nx] and graph[ny][nx] == 0:
                visit[ny][nx] = True
                graph[ny][nx] = 1
                zerocounter -= 1
                queue.append((ny,nx,day))
    if zerocounter != 0:
        print(-1)
    else: print(day)


def find_1(arr):
    global zerocounter
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                index_arr.append((y,x)) #넣어줄 때 기간 카운트를 하기 위해, 튜플로 넣어줌
            elif arr[y][x] == 0:
                zerocounter+=1
    if zerocounter == 0:
        return 'notomato'

bfs()