import math

# n을 3의 n승으로 표현, 9 > 3**2
n = int(math.log(int(input())))
paper = []

minus_count = 0
zero_count = 0
plus_count = 0

# 3**n × 3**n 크기의 2차원 배열 입력
for _ in range(3**n):
    # 문자열을 int로 변환하여 저장
    paper.append(list(map(int, input().split())))

def is_same_number(x, y, size):
    """
    (x, y)에서 시작하는 size×size 구역이
    모두 같은 값인지 검사
    """
    global minus_count, zero_count, plus_count

    # 첫 번째 원소를 기준값으로
    point_val = paper[x][y]

    # 구역 전체 검사
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != point_val:
                return False

    # 전부 같다면, 해당 값에 따라 카운트 증가
    if point_val == -1:
        minus_count += 1
    elif point_val == 0:
        zero_count += 1
    else:
        plus_count += 1
    return True

def slice_paper(x, y, depth):
    """
    (x, y)를 왼쪽 상단으로 하고,
    크기 = 3^depth 인 구역을 검사.
    만약 구역 전체가 같은 값이면 카운트 증가 후 종료.
    그렇지 않다면 3×3으로 나누어 재귀.
    """

    # 현재 구역 한 변의 길이
    size = 3**depth

    # base condition: size == 1 이거나 depth == 0 → 더 이상 분할 불가
    if size == 1 or depth == 0:
        # 어차피 size=1이면 is_same_number로 체크 시 바로 카운트 증가
        is_same_number(x, y, size)
        return

    # 만약 전부 같은 값이면 종료
    if is_same_number(x, y, size):
        return

    # 전부 같지 않으면 3×3 분할
    sub_size = size // 3
    for ix in range(3):
        for iy in range(3):
            new_x = x + ix * sub_size
            new_y = y + iy * sub_size
            slice_paper(new_x, new_y, depth - 1)
    
slice_paper(0,0,n)
print(minus_count)
print(zero_count)
print(plus_count)