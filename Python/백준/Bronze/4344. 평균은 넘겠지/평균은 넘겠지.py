C = int(input())
for i in range(C) :
	case = input().split(" ")
	students_num = int(case[0])
	case.pop(0)
	total_score = 0
	for j in range(students_num) : 
		total_score += int(case[j]) 
	avg_score = total_score/students_num
	count = 0
	for k in range(students_num) :
		if avg_score < int(case[k]) :
			count += 1
	print(round(count/students_num*100,3),"%")