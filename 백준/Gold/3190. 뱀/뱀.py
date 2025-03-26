import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = []
for i in range(k):
  x, y = map(int, sys.stdin.readline().split())
  apples.append((x, y))
l = int(sys.stdin.readline())
move_list = deque([])
for i in range(l):
  time, dir = sys.stdin.readline().split()
  move_list.append((int(time), dir))

next_move = move_list.popleft()

change_coor = [(0, 1), (1, 0), (0, -1), (-1, 0)]
now_dir = 0
def change_dir(direction):
  global now_dir
  if direction == 'D':
    now_dir += 1
  elif direction == 'L':
    now_dir -= 1
  if now_dir == 4:
    now_dir = 0
  elif now_dir == -1:
    now_dir = 3

snake_head = (1, 1)
snake = deque([snake_head])

proceed_time = 0
while snake_head[0] >= 1 and snake_head[1] >= 1 and snake_head[0] <= n and snake_head[1] <= n:
  proceed_time += 1
  snake_head = (snake_head[0] + change_coor[now_dir][0], snake_head[1] + change_coor[now_dir][1])
  if snake_head in snake:
    break
  snake.append(snake_head)
  if snake_head not in apples:
    snake.popleft()
  else:
    apples.remove(snake_head)
  
  if proceed_time == next_move[0]:
    change_dir(next_move[1])
    if move_list:
      next_move = move_list.popleft()

print(proceed_time)