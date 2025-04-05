import sys

input = sys.stdin.readline
n = int(input())

def fib(num):
    dp = [0,1] + [0] * (num-1)
    for i in range(2,num+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[num]

print(fib(n))