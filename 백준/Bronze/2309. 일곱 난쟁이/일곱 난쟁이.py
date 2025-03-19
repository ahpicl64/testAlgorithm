from itertools import permutations
import sys

sys.setrecursionlimit(10**8)


dwarfs = []

for i in range(9):
    dwarfs.append(int(sys.stdin.readline().strip('\n')))

permutated_list = list(permutations(dwarfs,7))

def find_dwarfs(arr):
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(7):
            sum += int(arr[i][j])
        if sum == 100:
            result = arr[i]
            return result

def print_result(arr):
    for i in range(len(arr)):
        print(arr[i])

result = sorted(find_dwarfs(permutated_list))
print_result(result)