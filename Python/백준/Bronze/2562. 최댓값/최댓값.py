max_num = 0
numbers = []


for i in range(9) : 
	number = int(input().replace(" ","")) 
	if max_num < number : 
		max_num = number
	numbers.append(number)

print(max_num)
print(numbers.index(max_num) + 1)