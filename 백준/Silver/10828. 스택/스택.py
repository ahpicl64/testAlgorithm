import sys


n = int(sys.stdin.readline().rstrip())
arr = []

def push(n):
    return arr.append(n)

def pop():
    if not len(arr) == 0:
        print (arr[-1])
        arr.pop(-1)
    else:
        print(-1)

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else : print(0)

def top():
    if not len(arr) == 0:
        print(arr[-1])
    else : print(-1)

for i in range(n):
    a = sys.stdin.readline().rstrip()

    if 'push' in a:
        a, n = map(str,a.split())
        n = int(n)
        push(n)
    if 'pop' in a:
        pop()
    if 'size' in a:
        size()
    if 'empty' in a:
        empty()
    if 'top' in a:
        top()
    