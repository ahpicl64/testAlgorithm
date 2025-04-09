n, k = map(int,input().split())
dp = [[0]*(n+1) for _ in range(n+1)]

def pas(n):
    for y in range(n+1):
        for x in range(n+1):
            if x == 0 or x == y:
                dp[y][x] = 1
            else:
                dp[y][x] = dp[y-1][x-1] + dp[y-1][x]

pas(n)
print(dp[n-1][k-1])
