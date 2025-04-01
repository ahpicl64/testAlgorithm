import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

class Graph:
    def __init__(self):
        self.list = {}

    def add_node(self, val):
        if val not in self.list:
            self.list[val] = []
    
    def add_edge(self, a, b):
        self.list[a].append(b)

g = Graph()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, field, visited, m, n):
    visited[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny, field, visited, m, n)



# 배추밭의 가로M, 세로N
for i in range(T):
    m, n, k = map(int,input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0
    for l in range(k):
        x, y = map(int,input().split())
        field[y][x] = 1

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and field[y][x] == 1:
                dfs(x, y, field, visited, m, n)
                count += 1
    
    g.list = {}
    print(count)
