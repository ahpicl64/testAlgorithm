"""
끼야호우
"""
from collections import deque
import sys

input = sys.stdin.readline
n = int(input()) # 1~ n-1 기본부품 및 중간 부품의 번호, n : 완제품 번호
m = int(input()) # x,y,k를 인풋받기 위한 반복 수
# 완제품, 또는 중간부품(x) = 기본부품(y) * k개

graph = {}
need = {}

for i in range(1,n+1):
    graph[i] = []
    need[i] = {}

for _ in range(m):
    x,y,k = map(int,input().split())
    graph[y].append((x,k))

indegree = [0] * (n+1)

# indegree 검출하는 로직
for parts in graph:
    for part,amounts in graph[parts]:
        indegree[part] += 1

queue = deque() # 큐 생성(indegree 0인 품목 제외)
for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    part = queue.popleft()  # 현재 부품
    for product, amount in graph[part]:
        if need[part]:
            # part가 중간 부품인 경우: 이미 누적된 기본 부품들을 전파
            for basic_part, count in need[part].items():
                if basic_part in need[product]:
                    need[product][basic_part] += count * amount
                else:
                    need[product][basic_part] = count * amount
        else:
            # part가 기본 부품인 경우: part 자체를 전파
            if part in need[product]:
                need[product][part] += amount
            else:
                need[product][part] = amount

        indegree[product] -= 1  # product의 indegree 감소
        if indegree[product] == 0:
            queue.append(product)

for part, amount in sorted(need[n].items()):
    print(f'{part} {amount}')