width, height = map(int,input().split(" "))

col_list = []
row_list = []

def check_cut_position(position, cut):
	position = position
	cut = cut
	if position == 0:
		row_list.append(cut)
	else:
		col_list.append(cut)
	return col_list, row_list
	
def sort_list(list):
	return list.sort()

def find_max(list):
	temp = list[0]
	for i in range(len(list)-1):
		if temp < (int(list[i+1])-int(list[i])):
			temp = (int(list[i+1])-int(list[i]))
	return temp
	
T = int(input())
for i in range(T):
	position, cut = map(int,input().split(" "))
	check_cut_position(position, cut)
	
sort_list(col_list)
sort_list(row_list)

col_list.append(width)
row_list.append(height)

print (find_max(col_list)*find_max(row_list))