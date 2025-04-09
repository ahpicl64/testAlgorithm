import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n

def solder():
    for i in range(n): # list를 하나 씩 옮겨가는 포인터
        for j in range(i): # 앞에서부터 옮겨가면서 dp 카운터를 올려주는 역할
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return

solder()

result = max(dp)

print(n-result)