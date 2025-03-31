from collections import deque
import sys

input = sys.stdin.readline
computer = int(input())
connect = int(input())

class Graph:
    def __init__(self):
        self.list = {}

    def add_node(self, a):
        if a not in self.list:
            self.list[a] = []

    def add_edge(self, a,b):
        self.add_node(a)
        self.add_node(b)

        self.list[a].append(b)
        self.list[b].append(a)

g = Graph()

def bfs(node):
    count = -1
    visited = set()
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            count+=1
            visited.add(node)
            for neighbor in g.list.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return count

for _ in range(connect):
    a, b = map(int,input().split())
    g.add_edge(a,b)

print(bfs(1))