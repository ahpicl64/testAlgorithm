import sys

input = sys.stdin.readline
n = int(input())

def fib(num):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,num+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[num]

print(fib(n))