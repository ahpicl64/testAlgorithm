# from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())

graph = [list(map(int,list(input().replace('-','0').replace('|','1').strip()))) for _ in range(n)]
visit = [[False] * m for _ in range(n)] 
# print(graph)
result = []

# def bfs(y,x):
#     count = 1
#     for x in range(1,n):
#         if graph[y][x] != graph[y][x-1]:
#             count+=1
#     result.append(count)
#     return
count = 0
def bfs_x(y):
    global count
    if graph[y][0] == 0:
        count += 1
    for x in range(1,m):
        if graph[y][x] == 0 and graph[y][x-1] == 1:
            count += 1

def bfs_y(x):
    global count
    if graph[0][x] == 1:
        count += 1
    for y in range(1,n):
        if graph[y][x] == 1 and graph[y-1][x] == 0:
            count += 1


for y in range(n):
    bfs_x(y)
for x in range(m):
    bfs_y(x)
    
print(count)