import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int,input().split())

class Graph:
    def __init__(self):
        self.list = {}

    def add_node(self, val):
        if val not in self.list:
            self.list[val] = []

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        self.list[a].append(b)

visited = [False] * (n+1)
g = Graph()
result = []

def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for neighbor in g.list.get(node, []):
        dfs(neighbor)
    
    result.append(node)


for i in range(m):
    a, b = map(int,input().split())
    g.add_edge(a,b)

for i in range(1,n+1):
    dfs(i)

result.reverse()
    
for node in result:
    print(node, end = " ")