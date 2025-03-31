import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

v, e = map(int,input().split()) # 총 노드 개수와, 간선 개수 저장
# 노드 개수는 이후 이진트리 완성 후 선택된 간선들의 집합 길이가 node-1인지 판별하는데 사용
parent = list(range(v+1))
tree = []
weight_sum = 0
edges = []

def make_set(x):
    parent[x] = x

# x의 대표(루트) 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(edge,x,y):
    global weight_sum
    # 같은 루트일 때 유니온하게되면, cycle 형성
    parent_x = find(x)
    parent_y = find(y)
    if parent_x == parent_y:
        return
    tree.append(edge)
    weight_sum += edge[0]
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y
    return

for _ in range(e):
    start, destination, weight = map(int, input().split())
    edges.append([weight, start, destination])
    make_set(start)
    make_set(destination)

edges.sort()

for edge in edges:
    union(edge, edge[1], edge[2])
    if len(tree) == v - 1:
        break

print(weight_sum)