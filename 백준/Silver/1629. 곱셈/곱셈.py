import sys
sys.setrecursionlimit(10**5)

a,b,c = map(int,sys.stdin.readline().rstrip().split())

def mod_pow(a, b, c):
    result = 1
    a = a % c  # 처음에 a를 mod c로 만들기
    while b > 0:
        # b가 홀수이면 result에 a를 곱하고 mod c를 적용
        if b % 2 == 1:
            result = (result * a) % c
        # a를 제곱하고 mod c를 적용
        a = (a * a) % c
        b //= 2
    return result

print(mod_pow(a, b, c))