from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int,input().split())

maze = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

visited[0][0] = True
distance[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append((0,0))


while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))



print(distance[n-1][m-1])