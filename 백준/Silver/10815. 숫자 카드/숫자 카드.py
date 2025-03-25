import sys


t = int(input())
card = list(map(int,sys.stdin.readline().rstrip().split()))
card.sort()

M = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

def find_card(target,left,right):
    if left > right:
        print(0, end=' ')
        return
    
    center = (left+right) // 2

    if card[center] == target:
        print(1, end=' ')
        return 
    elif card[center] > target:
        find_card(target, left, center-1)
    elif card[center] < target:
        find_card(target, center+1,right)

for i in range(len(targets)):
    find_card(targets[i],0,t-1)