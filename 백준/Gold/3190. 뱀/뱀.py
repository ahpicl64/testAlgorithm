from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())      # 보드판의 크기
K = int(sys.stdin.readline().rstrip())      # 사과의 개수
board = [[0] * N for _ in range(N)] # 보드 만들기 

# 사과 위치 지정, 사과가 있는 칸은 1, 없는 칸은 0
for i in range(K):
    row,col = map(int,sys.stdin.readline().rstrip().split())
    row -= 1
    col -= 1
    board[row][col] = 1

# 뱀 초기위치 설정
snake = deque([(0,0)])
board[0][0] = 2 # 뱀이 위치하고 있는 위치는 2로 표기
second = 0 # 시간 초기 설정

# 방향전환을 rotate로 구현
dirrection = deque([('right'),('down'),('left'),('up')]) 
dir_change = []

L = int(sys.stdin.readline().rstrip())      # 뱀의 움직임의 횟수
# 방향 전환 방식 저장
for i in range(L):
    time, change = map(str,sys.stdin.readline().rstrip().split())
    time = int(time)
    dir_change.append([time,change])


def set_dir(C):
    if C == 'L':
        dirrection.rotate(1)
    elif C == 'D':
        dirrection.rotate(-1)

def move(row,col):
    if row < 0 or row >= N or col < 0 or col >= N:
        return False

    if board[row][col] == 2: # 꼬리가 있으므로, 게임 종료
        return False
    
    if board[row][col] == 1: # 사과가 있으므로, pop 수행 x
        snake.append((row,col))
        board[row][col] = 2 # 사과를 먹고, 머리가 위치하므로 2로 변경
        return True

    if board[row][col] == 0: # 사과가 없으므로, popleft 수행
        snake.append((row,col))
        #pop 되기 전 별도의 변수로 저장(board = 0으로 변경)
        tail_row = snake[0][0]
        tail_col = snake[0][1]
        snake.popleft()
        board[tail_row][tail_col] = 0 # 뱀 꼬리가 지나갔으므로, 0으로 변경
        board[row][col] = 2 # 뱀 머리가 위치했으므로, 2로 변경
        return True

def snake_game():
    global second
    row = 0
    col = 0
    # 게임이 끝날때 까지 반복, 게임이 끝나는 조건은 별도로 break
    while True:
        # 초에 따른 움직임은, for 문으로 구현
        # 움직임을 받는 함수 별도로? 일단 내부에 구현
        second += 1 # while문이 동작할 때 마다 1초씩 지나는 것으로 간주

        if dirrection[0] == 'right':
            col += 1
        if dirrection[0] == 'down' :
            row += 1
        if dirrection[0] == 'left' :
            col -= 1
        if dirrection[0] == 'up' :
            row -= 1

        if move(row,col) == False :
            break

        if dir_change and dir_change[0][0] == second:
            set_dir(dir_change[0][1])
            dir_change.pop(0)

snake_game()

print(second) # break로 while문 탈출 시 print 후 종료
