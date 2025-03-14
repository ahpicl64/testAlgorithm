T = int(input())

for i in range(T):
	repeat_num, string = input().split(" ")
	word = list(string)
	n = len(word)
	for j in range(n):
		word[j] = word[j] * int(repeat_num)
		result = ''.join(word)
	print(result)
