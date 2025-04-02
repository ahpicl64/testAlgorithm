import heapq
import sys

class Graph:
    def __init__(self):
        self.list = {}
    
    def add_node(self, value):
        if value not in self.list:
            self.list[value] = []

    def add_edge(self, a, b, weight):
        self.add_node(a)
        self.add_node(b)

        self.list[a].append((weight,b))

input = sys.stdin.readline
n = int(input())
m = int(input())
g = Graph()
for i in range(m):
    a, b, w = map(int,input().split())
    g.add_edge(a,b,w)

distance = [float('inf')] * (n+1)

def dijkstra(start):
    distance[start] = 0
    heap = [(0,start)]

    while heap:
        curr_distance, curr_node = heapq.heappop(heap)
        if curr_distance > distance[curr_node] :
            continue
        for weight, neighbor in g.list[curr_node]:
            nd = curr_distance + weight
            if nd < distance[neighbor]:
                distance[neighbor] = nd
                heapq.heappush(heap, (nd, neighbor))

start, destination = map(int,input().split())
dijkstra(start)
print(distance[destination])