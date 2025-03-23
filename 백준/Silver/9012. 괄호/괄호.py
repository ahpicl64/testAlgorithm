import sys

T = int(sys.stdin.readline().rstrip())


#테스트 개수 만큼 문자열 검증
for i in range(T):
    #스택에 넣기 전 원본 그대로의 배열
    arr = list(sys.stdin.readline().rstrip())
    stack = []
    for j in range(len(arr)):
        if arr[j] == ')' and len(stack) == 0:
            print('NO')
            break
        elif arr[j] == ')' and len(stack) != 0:
            stack.pop()
        elif arr[j] == '(':
            stack.append(arr[j])
    else:
        if len(stack) == 0:
            print('YES')
        else : print('NO')