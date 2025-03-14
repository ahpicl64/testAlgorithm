a,b,v = map(int,input().split(' '))
check = (v - a) % (a - b) 
day = ((v - a) / (a - b)) + 1
if v <= a : 
	print(1)
elif check == 0 : 
	print(int(day))
else :
	print(int(day)+1) 