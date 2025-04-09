import sys

input = sys.stdin.readline

X = list(input().rstrip())
Y = list(input().rstrip())

# print (X)
# print (Y)

def lcs(x,y):
    m,n = len(X), len(Y) # 인덱스 생성
    # DP 배열 생성
    dp = [[0]*(m+1) for _ in range(n+1)]

    
    # dp 배열에 수 채워주기
    for i in range(1,n+1):
        for j in range(1,m+1):
            # x축, y축 문자열이 같을 때. 현재 보고있는 dp테이블의 수를 좌상단에서 +1해줌
            if X[j-1] == Y[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # 같지 않을 때, 위, 좌측을 검사해서 큰 값을 넣어주기
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return print(dp[n][m])

lcs(X,Y)