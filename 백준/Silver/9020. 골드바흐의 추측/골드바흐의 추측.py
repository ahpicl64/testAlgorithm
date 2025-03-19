T = int(input())

num = 0

def find_prime(num):
	prime_nums = [True for i in range (num+1)]
	prime_nums[0] = prime_nums[1] = False

	for i in range(2, int(num ** (1/2)) + 1):
		if prime_nums[i]: 
			for j in range(i*i, num + 1, i):
				prime_nums[j] = False

	result = []
	for k in range(len(prime_nums)):
		if prime_nums[k]:
			result.append(k)
	return result

def find_partition(prime):
    for i in range(num // 2, 1, -1):
        j = num - i
        if i in prime and j in prime:
            return str(i) + " " + str(j)

for i in range(T):
	num = int(input())
	print(find_partition(find_prime(num)))