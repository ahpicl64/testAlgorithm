
import sys

T = int(sys.stdin.readline().rstrip())
arr = []

def pop():
    arr.pop(-1)

def push(num):
    arr.append(num)

for i in range(T):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        pop()
    else :
        push(a)

print(sum(arr))