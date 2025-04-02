from collections import deque
import sys

input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.list = {}

    def add_nodes(self, v):
        for i in range(1,v+1):
            self.list[i] = []
    
    def add_edges(self, a, b):
        self.list[a].append(b)
        self.list[b].append(a)


K = int(input())
checker = True


def bfs(node, color):
    queue = deque([node])
    color[node] = 1
    while queue:
        curr_node = queue.popleft()
        for neighbor in g.list.get(curr_node,[]):
            if color[neighbor] == 0:
                color[neighbor] = 3 - color[curr_node]
                queue.append(neighbor)
            elif color[neighbor] == color[curr_node]: 
                return False
    return True

for _ in range(K):
    V, E = map(int,input().split())
    g = Graph()
    g.add_nodes(V)
    for _ in range(E):
        a, b = map(int,input().split())
        g.add_edges(a,b)

    color = [0]*(V+1)
    checker = True
    for i in range(1,V+1):
        if color[i] == 0:
            if not bfs(i, color):
                checker = False
                break

    if checker:
        print('YES')
    else: print('NO')

    checker = True