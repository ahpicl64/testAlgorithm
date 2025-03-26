import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())

def insert_data(num):
    heapq.heappush(heap,num)

def read_data():
    if len(heap) == 0:
        return print(0)
    else : 
        return print(heapq.heappop(heap))

for _ in range(n):
    val = int(input())
    if val == 0:
        read_data()
    else :
        insert_data(val)