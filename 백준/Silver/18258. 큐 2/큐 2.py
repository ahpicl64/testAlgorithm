from collections import deque
import sys


T = int(sys.stdin.readline().rstrip())
arr = deque()

def push(val):
    arr.append(val)

def pop():
    if len(arr) == 0:
        print(-1)
    else :
        print(arr[0])
        arr.popleft()

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(arr) != 0:
        print(arr[0])
    else:
        print(-1)

def back():
    if len(arr) != 0:
        print(arr[-1])
    else:
        print(-1)

for i in range(T):
    command = sys.stdin.readline().rstrip().split()
    num = 0
    if 'push' in command:
        command, num = map(str, command)
        num = int(num)
        push(num)
    elif 'pop' in command:
        pop()
    elif 'size' in command:
        size()
    elif 'empty' in command:
        empty()
    elif 'front' in command:
        front()
    elif 'back' in command:
        back()