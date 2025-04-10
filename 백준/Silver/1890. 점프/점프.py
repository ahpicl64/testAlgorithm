import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (n) for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        jump = arr[i][j]
        left_x = n-1-j
        left_y = n-1-i

        nx = j + jump
        ny = i + jump

        if ny <= (n-1) and arr[i][j] != 0 :
            dp[ny][j] += dp[i][j]
        if nx <= (n-1) and arr[i][j] != 0 :
            dp[i][nx] += dp[i][j]

print(dp[n-1][n-1])