import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
class Graph:
    def __init__(self):
        self.list = {}
        self.parents = {}
    
    def add_nodes(self, val):
        if val not in self.list:
            self.list[val] = []
            self.parents[val] = 0

    def add_edges(self, a, b):
        self.add_nodes(a)
        self.add_nodes(b)

        self.list[a].append(b)
        self.list[b].append(a)

    def add_parents(self, parent, child):
        self.parents[child] = parent

visited = [False] * (N+1)
g = Graph()

def dfs(node):
    if visited[node]:
        return
    
    visited[node] = True
    for neighbor in g.list.get(node, []):
        if not visited[neighbor]:
            g.add_parents(node, neighbor)
            dfs(neighbor)

for i in range(N-1):
    a, b = map(int,input().split())
    g.add_edges(a,b)

dfs(1)

for i in range(2, N+1):
    print(g.parents[i])