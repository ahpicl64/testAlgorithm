import sys

input = sys.stdin.readline

N,K = map(int,input().split())
items = []
for _ in range(N):
    W, V = map(int,input().split())
    items.append((W,V))

dp = [0] * (K+1) # 배열 길이 = 무게

for weight, value in items:
    for w in range(K, weight-1, -1): # dp 뒤에서부터 넣어주기
        dp[w] = max(dp[w], dp[w - weight] + value)
print(max(dp))