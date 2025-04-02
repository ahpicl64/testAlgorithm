from collections import deque
m,n,h = map(int,input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[False] * m for _ in range(n)] for _ in range(h)]
index_arr = []
zerocounter = 0
def bfs():
    global zerocounter
    queue = deque()
    if find_1(graph) == 'notomato':
        return print(0)
    for i in range(len(index_arr)):
        z, y, x = index_arr[i]
        visit[z][y][x] = True
        queue.append((z,y,x,-1))
    while queue:
        z, y, x, day = queue.popleft()
        day += 1
        for dz,dy,dx in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            nz,ny,nx = z + dz, y + dy, x + dx
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and not visit[nz][ny][nx] and graph[nz][ny][nx] == 0:
                visit[nz][ny][nx] = True
                graph[nz][ny][nx] = 1
                zerocounter -= 1
                queue.append((nz,ny,nx,day))
    if zerocounter != 0:
        print(-1)
    else: print(day)


def find_1(arr):
    global zerocounter
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if arr[z][y][x] == 1:
                    index_arr.append((z,y,x)) #넣어줄 때 기간 카운트를 하기 위해, 튜플로 넣어줌
                elif arr[z][y][x] == 0:
                    zerocounter+=1
    if zerocounter == 0:
        return 'notomato'

bfs()