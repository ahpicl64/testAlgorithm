import heapq
import sys


input = sys.stdin.readline
n = int(input())

heap = []

for _ in range(n):
    row = list(map(int,input().split()))
    for num in row:
        if len(heap)<n: #힙의 크기가 n보다 작을때는 그냥 push
            heapq.heappush(heap,num)
        else : 
            if num > heap[0]: # 힙의 가장 작은값과 비교, 만약 들어오는 값이 더 크면 넣기
                heapq.heappushpop(heap,num)

print(heap[0])