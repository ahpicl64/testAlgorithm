import sys


T, M = map(int,sys.stdin.readline().rstrip().split()) # depth 깊어질 수록 input() 사용 시 시간초과 방지

wood_arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 입력받은 벌목 허가받은 나무들 배열 생성 
wood_arr.sort() # 벌목 대상 나무 배열정렬
max_wood_height = wood_arr[-1] # 벌목 허가된 나무 중 가장 높은 값 변수 선언
cutter_set_arr = [] # 목재절단기 높이 설정 탐색위한 빈 배열 생성(none)
target = 0


# 사용 메모리가 많아 수정
# # 목재 절단기 탐색범위(min~가장 큰 나무 길이) 생성 함수
# # 가장 작은 나무 길이 ~ 가장 큰 나무 길이
# def make_cutter_range_arr(min, max):
#     global cutter_set_arr
#     for i in range(min, max+1):
#         cutter_set_arr.append(int(i))
#     return cutter_set_arr


# 벌목 설정 높이 탐색 후 최적값(M값보다) 검증 로직
def check_cutter_height(arr, num):  # 벌목대상 나무 크기 배열, 벌목 설정높이
    sum_num = 0 # 설정높이로 잘랐을 때, 나오는 값들 더해줄 예정
    for i in range(len(arr)):
        result = arr[i] - num # 나무별 높이로 잘라주기
        if result < 0:
            result = 0
        sum_num += result # 각 값을 더해줘서
    if sum_num >= M: # 세팅대로 잘랐을 때 가져가야할 나무 길이 M보다 큰지 판별
        return True
    return False

def set_height(min, max):
    global target
    pc = (min + max) // 2  # 포인터 생성 (중앙값)
    # base case : pl == pr, or pl > pr , 더 이상 탐색 범위가 없을 때
    if min > max:
        # 리턴값 고민 필요. 
        return target

    # 포인터 조정 구간은, 최적값 검증 로직 통과 후 
    # 목표하는 값 이상을 얻었을 때(정답은 가능하지만 더 높은값 탐색이 필요)
    elif check_cutter_height(wood_arr, pc) == True: # (검증로직에 의한 결과값이 >= M 일 때)
        # 별도로 target 값을 그때그때 arr[pc]로 덮어씌워줄 필요
        if target < pc:
            target = pc
    # 검증 로직 필요
        set_height(pc+1, max)
    
    # 목표하는 값이 아닐 때(더 낮은값 탐색이 필요)
    elif check_cutter_height(wood_arr, pc) == False: # (검증로직에 의한 결과값이 < M 일 때)
        set_height(min, pc-1)


# make_cutter_range_arr(min_wood_height, max_wood_height)
set_height(0, max_wood_height)
print(target)