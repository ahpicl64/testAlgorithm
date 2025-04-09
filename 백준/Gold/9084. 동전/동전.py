import sys

input = sys.stdin.readline

T = int(input())


#테스트 케이스 만큼 함수 실행
for i in range(T):
    n = int(input()) #코인의 개수
    coins = list(map(int,input().split())) # 코인들 배열 생성
    m = int(input()) # 생성할 금액
    dp = [0]*(m+1) # 배열의 길이는 코인의 금액 만큼
    dp[0] = 1 # 0원은 가지수가 1
    
    for coin in coins:
        for j in range(coin, m+1):
            dp[j] += dp[j-coin]

    print(dp[m])