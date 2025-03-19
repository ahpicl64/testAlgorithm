target_num = int(input())
count = 0
for i in range(target_num):
	check_num = list(str(i+1)) 
	
	if len(check_num) == 1 or len(check_num) == 2:
		count+=1
	elif len(check_num) == 3:
		if int(check_num[1])-int(check_num[0]) == int(check_num[2])-int(check_num[1]):
			count+=1

print(count)	