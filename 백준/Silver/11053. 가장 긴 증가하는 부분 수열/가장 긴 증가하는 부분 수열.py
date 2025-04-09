import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

dp = [1] * n
def lis():
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return

lis()
print(max(dp))