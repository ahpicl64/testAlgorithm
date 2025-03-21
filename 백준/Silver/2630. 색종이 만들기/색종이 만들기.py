n = int(input())
white_count = 0
blue_count = 0
#길이 = n
origin_paper = [list(map(int,input().split())) for _ in range(n)]

def cut_paper(x,y,n):
		#base condition
    if is_same_color(x,y,n) or n==0:
        return
    small_length = n//2
    cut_paper(x,y,small_length)
    cut_paper(x+small_length,y,small_length)
    cut_paper(x,y+small_length,small_length)
    cut_paper(x+small_length,y+small_length,small_length)

def is_same_color(x,y,n): #배열, 길이
    global white_count, blue_count
    first_val = origin_paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if origin_paper[i][j] != first_val:
                return False
    if first_val == 0:
        white_count+=1
    else :
        blue_count+=1
    return True


cut_paper(0,0,n)
print(white_count)
print(blue_count)