def is_prime_num (num):
	if num == 1: return False
	for i in range(2,int(num**(1/2))+1):
		if num % i == 0:
			return False
	return True

T = int(input())
numbers = input().split(" ")
counter = 0
for i in range(T):
	num = int(numbers[i])
	if is_prime_num(num) == True:
		counter += 1
print(counter)