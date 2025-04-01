from collections import deque
import sys


input = sys.stdin.readline

M, N = map(int,input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(M)]

visit = [[False] * N for _ in range(M)]

def bfs():
    queue = deque()
    for x in range(N):
        if graph[0][x] == 0 and not visit[0][x]:
            visit[0][x] = True
            queue.append((0,x))
    while queue:
        current_y, current_x = queue.popleft()
        if current_y == (M-1):
            print('YES')
            return
        for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny, nx = current_y + dy, current_x + dx
            if 0 <= ny < M and 0 <= nx < N and not visit[ny][nx] and graph[ny][nx] == 0:
                visit[ny][nx] = True
                queue.append((ny,nx))

    print('NO')

bfs()