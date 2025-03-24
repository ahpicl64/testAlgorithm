from collections import deque
import sys


numbers = deque()
n,T = map(int, sys.stdin.readline().rstrip().split())

for i in range(1,n+1):
    numbers.append(i)
arr = deque()

while len(numbers) != 0:
    for i in range(len(numbers)):
        numbers.rotate(-T+1)
        arr.append(numbers.popleft())

result = f"<{str(arr).lstrip('deque([').rstrip('])')}>"
print(result)