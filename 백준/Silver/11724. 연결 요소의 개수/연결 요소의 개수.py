import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int,input().split())

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, val):
        if val not in self.nodes:
            self.nodes[val] = []
    
    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)

        self.nodes[a].append(b)
        self.nodes[b].append(a)

def dfs(node):
    if visited[node]:
        return
    
    visited[node] = True

    for neighbor in g.nodes.get(node, []):
        if not visited[neighbor]:
            dfs(neighbor)
        
g = Graph()
visited = [False] * (N+1)
count = 0

for i in range(M):
    a, b = map(int,input().split())
    g.add_edge(a,b)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)