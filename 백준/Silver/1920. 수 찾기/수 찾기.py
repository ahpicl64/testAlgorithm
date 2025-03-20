import sys

test_count = int(input())
check_numbers = list(map(int,input().split(" ")))
check_numbers.sort()
rounds = int(input())
target_nums = list(map(int,input().split(" ")))


def search(arr,num,pl,pr):
    pc = (pl + pr) // 2

    if arr[pc] == num:
        return print(1)
    elif pl > pr:
        return print(0)
    elif arr[pc] < num:
        search(arr,num,pc+1,pr)
    elif arr[pc] > num:
        search(arr,num,pl,pc-1)
    

for i in range(rounds):
    length = len(check_numbers)
    num = target_nums[i]
    search(check_numbers,num,0,length-1)