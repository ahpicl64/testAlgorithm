number = input().split()
reverse_num = []
for i in range(2) :
	reverse_num.append(int(number[i][::-1]))
	
if int(reverse_num[0]) < int(reverse_num[1]):
	print (reverse_num[1])
else :
	print (reverse_num[0])