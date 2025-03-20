#점화식 도출
# input -> output
# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 7
# 5 -> 13...
# n = (n-1) + (n-2) + (n-3)

# 테스트 횟수
T = int(input())

def get_plus_num(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	else:
		return get_plus_num(n-1)+get_plus_num(n-2)+get_plus_num(n-3)	
		

for i in range(T):
    n = int(input())
    print(get_plus_num(n))