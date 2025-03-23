import sys

# 테스트 케이스 횟수 선언
T = int(sys.stdin.readline().rstrip())

peak = 0
count = 0

# 막대기 높이를 저장할 stack 생성
stack = []
for i in range(T):
    a = int(sys.stdin.readline().rstrip())
    stack.append(a)

# stack을 순회하며 보이는 막대기 수를 측정
for j in range(len(stack)-1,-1,-1):
    # 전역변수 접근 가능하도록
    if stack[j] > peak :
        peak = stack[j]
        count +=1
print(count)    