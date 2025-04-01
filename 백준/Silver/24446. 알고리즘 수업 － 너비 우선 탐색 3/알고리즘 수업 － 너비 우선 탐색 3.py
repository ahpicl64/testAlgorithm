from collections import deque
import sys


input = sys.stdin.readline
N, M, R = map(int,input().split())


class Graph:
    def __init__(self):
        self.list = {}
    
    def add_node(self, val):
        for i in range(1,val+1):
            self.list[i] = []
    
    def add_edge(self, a, b):
        # self.add_node(a)
        # self.add_node(b)

        self.list[a].append(b)
        self.list[b].append(a)

visit = [False] * (N+1)
depth = [-1] * (N+1)

g = Graph()
g.add_node(N)


# 입력값 그래프 생성 함수
for i in range(M):
    a,b = map(int,input().split())
    g.add_edge(a,b)

def bfs(node):
    # if visit[node]:
    queue = deque([(node,0)])
    visit[node] = True
    depth[node] = 0

    while queue:
        node, cur_depth = queue.popleft()
        for neighbor in g.list[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                depth[neighbor] = cur_depth + 1
                queue.append((neighbor, cur_depth + 1))
    return

bfs(R)
for i in range(1,N+1):
    print(depth[i])