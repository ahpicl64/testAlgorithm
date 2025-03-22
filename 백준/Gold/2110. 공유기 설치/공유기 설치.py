# 집 좌표가 주어짐
# 집 위치 배열을 오름차순으로 정렬
# 기본적으로 각 와이파이중 2대는 집 배열의 0과 마지막에 위치 (아님)
# 결과 값은 각 집 간의 거리를 고르게 분포시키되, 그중에서 가장 짧은 값을 도출
# 집간의 간격 배열을 도출.?
# 탐색 범위는 집좌표 x[0] ~ x[n] 까지 탐색 시작
# x[0]은 기본적으로 공유기 1대가 위치한다고 가정
# x[0]에 설치한 공유기와 그 다음에 설치한 공유기의 거리의 최소값을 찾는것으로 가정하고
# 검증논리는 그 최소값을 활용 했을 때 다른 공유기들의 설치댓수가 나오는지,
# base case는 탐색 범위가 더이상 없을 때 까지


import sys


T, C = map(int, sys.stdin.readline().rstrip().split()) # 집의 개수와 공유기의 개수 선언
home_positions = []
for i in range(T):
    home_positions.append(int(sys.stdin.readline().rstrip())) # 집 거리 배열 생성
home_positions.sort()  # 집 좌표 오름차순 정렬
max_position = home_positions[-1] # 가장 먼 집의 좌표 변수선언

# 와이파이 설치 가능 댓수로 최소값 가능성 찾는 검증 로직
# True 리턴받는다면, 가능값 ()
# False 리턴받는다면, 불가능값
# 최초 0에 설치, distance 만큼 거리 이상의 값을 가진 집 위치를 찾아 설치
def is_min_distance(distance):
    install_count = 1
    left_home = 0 # 최초 설치되는 집의 위치 idx
    right_home = 1 # 바로 다음 거리 집의 위치 idx
    while right_home < len(home_positions):
        if home_positions[right_home] - home_positions[left_home] >= distance: # 왼쪽집과 우측집 최소거리 설치가 가능하다면
            install_count += 1 # 설치대수 1 증가
            left_home = right_home #
            right_home += 1
        elif home_positions[right_home] - home_positions[left_home] < distance:
            right_home += 1 # 설치 거리만 늘려주기
    
    if install_count >= C:
        return True
            
    else: return False

def search_distance(arr,min,max):
    result = 0 #결과값 누적 갱신용 변수 선언
    while min <= max:
        pc = (min+max) // 2
        
        if is_min_distance(pc) == True: # 검증 로직 순회 후, True 반환 시 현재 가능성있는 결과값을 선언
            min = pc+1
            result = pc
        elif is_min_distance(pc) == False: # False 반환 시, 검색범위 조정
            max = pc-1

    return result

print(search_distance(home_positions, 0, max_position))
