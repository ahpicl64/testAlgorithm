from collections import deque
import sys

arr = deque(maxlen = 500000)
n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    arr.append(i)

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])