num_mount, target_num = map(int,input().split())
numbers = input().split()
i = 0
for i in range(num_mount) : # num mount만큼 반복
	number = int(numbers[i])
	if number < target_num :
		print (number, end=" ")
		
	i+1