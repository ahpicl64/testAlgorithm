import sys
import heapq

input = sys.stdin.readline
n = int(input())
q = []

def insert_item(item):
    heapq.heappush(q,-item)

def get_item():
    return -heapq.heappop(q)

for n in range(n):
    a = int(input())
    if a == 0:
        if len(q) == 0:
            print(0)
        else:
            print(get_item())
    else:
        insert_item(a)