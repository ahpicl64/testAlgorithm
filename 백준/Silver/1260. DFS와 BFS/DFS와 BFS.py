from collections import deque
import sys

input = sys.stdin.readline

v, e, root = map(int,input().split())

class Graph:
    def __init__(self):
        self.list = {}

    def add_vertex(self, a):
        if a not in self.list:
            self.list[a] = []

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)

        self.list[a].append(b)
        self.list[b].append(a)


def dfs(node, visited = None):
    if visited is None:
        visited = set()
    
    if node in visited:
        return
    
    print(node, end=" ")
    visited.add(node)

    for neighbor in sorted(g.list.get(node, [])):
        dfs(neighbor, visited)

def bfs(node):
    visited = set()
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end = " ")
            visited.add(node)
            for neighbor in sorted(g.list.get(node, [])):
                if neighbor not in visited:
                    queue.append(neighbor)

g = Graph()

for i in range(e):
    a, b = map(int,input().split())
    g.add_edge(a, b)
    
dfs(root)
print()
bfs(root)