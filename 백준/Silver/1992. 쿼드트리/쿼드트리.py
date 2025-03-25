
import sys


T = int(input())

arr = [list(map(str,list(sys.stdin.readline().rstrip()))) for _ in range(T)]

def is_same(row,col,n): # 검증할 배열과 그 크기를 지정
    target = arr[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if target != arr[i][j]:

                return False
    print(target, end='')
    return True


def quadtree(row,col,n):
    if is_same(row,col,n) == True:
        return
    else :
        print('(', end='')
        quadtree(row,col,n//2)
        quadtree(row,col+n//2,n//2)
        quadtree(row+n//2,col,n//2)
        quadtree(row+n//2,col+n//2,n//2)
    print(')', end='')

quadtree(0,0,T)