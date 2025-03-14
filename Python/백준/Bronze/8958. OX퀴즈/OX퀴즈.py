T = int(input()) # 최초 입력되는 테스트 케이스의 수

# 폐기. test를 위한 문자열은 한번에 나오기 때문에. 받는 순간 String별로 list해야함

# list가 2개 있어야함. answer score
# score 필요없음. 
for i in range(T): # 테스트 케이스 순회하는 반복문
	answer = list(input())	# 받아서 글자별로 정답 list
	length = len(answer)	# list의 length 변수 지정
	
	count = 0
	score = 0
	for n in range(length):	# length만큼 반복
		if answer[n] == "O": 	# O가 나올 때 마다 count 올려서 점수 추가
			count += 1 # count를 1 올림
			score += count # score에 누적시킴
		else:
			count = 0		# X가 나오면 count = 0으로 리셋
	print(score)