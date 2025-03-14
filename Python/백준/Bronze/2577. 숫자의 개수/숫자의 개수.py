a = int(input())
b = int(input())
c = int(input())
numlist = list(str(a*b*c))

for i in range(10) : 
	print(numlist.count(str(i)))