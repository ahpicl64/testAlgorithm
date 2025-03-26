import sys
circle_num = int(sys.stdin.readline().rstrip())
circle_position = [] #start, end
area = 1 + circle_num
for circle_index in range(circle_num):
  center, r = map(int, sys.stdin.readline().split())
  circle_position.append((center - r, center + r))
#원의 양 끝점 => 오른쪽 끝 오름차순, 왼쪽 시작 내림차순
circle_position.sort(key=lambda x: (x[1], -x[0]))
left_stack = []
right_stack = []
# print(circle_position)
for circle_index in range(circle_num):
  if(left_stack and left_stack[-1] > circle_position[circle_index][0] and right_stack[-1] < circle_position[circle_index][1]):
    while(left_stack and left_stack[-1] > circle_position[circle_index][0] and right_stack[-1] < circle_position[circle_index][1]):
      left_stack.pop()
      right_stack.pop()
  ## 빈스택인 경우
  if not left_stack:
    left_stack.append(circle_position[circle_index][0])
    right_stack.append(circle_position[circle_index][1])
    continue
  #오른쪽 같으면
  if circle_position[circle_index][1] == right_stack[-1]:
    ## 오른쪽이 같은데 stack이 한개인경우
    if(len(right_stack) == 1):
        right_stack.pop()
        left_stack.pop()
    # 대각선 타고 내려가다가 왼쪽 끝이 연결 안된경우 스택 비우기 필요
    elif(left_stack[0] > circle_position[circle_index][0]):
      while left_stack:
            left_stack.pop()
            right_stack.pop()
    else:
      #스택 길이 확인, 대각선으로 같은지 확인
      if len(right_stack) >= 2 and left_stack[-1] == right_stack[-2]:
        level_down = 0
        while len(right_stack) >= 2 + level_down and right_stack[-1] > circle_position[circle_index][0]:
        #대각선 값이 다르면 내부 원 모두 삭제
          if left_stack[-1-level_down] != right_stack[-2-level_down]:
            while left_stack and  left_stack[-1] >= circle_position[circle_index][0]:
              left_stack.pop()
              right_stack.pop()
            break
        #왼쪽 시작점이 현재 시작점과 같으면 사이에 있는 값 모두 pop한 뒤 영역+1
          if left_stack[-2-level_down] == circle_position[circle_index][0]:
            while left_stack and left_stack[-1] >= circle_position[circle_index][0]:
              left_stack.pop()
              right_stack.pop()
            area += 1
            break
          level_down += 1
    #대각선으로 다르면 Pop
      else:
        while left_stack and left_stack[-1] >= circle_position[circle_index][0]:
          left_stack.pop()
          right_stack.pop()
  #왼쪽 같으면
  elif circle_position[circle_index][0] == left_stack[-1]:
    left_stack.pop()
    right_stack.pop()
  left_stack.append(circle_position[circle_index][0])
  right_stack.append(circle_position[circle_index][1])
print(area)