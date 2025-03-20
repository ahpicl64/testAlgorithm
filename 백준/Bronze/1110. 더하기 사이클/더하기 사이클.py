n = input() #26
count = 0

def get_cycle(num):
    checknum = []
    compare_num = ""
    global count
    if int(num) < 10:
        checknum = ['0',num]
    else : 
        checknum = list(num) #['2','6']
    while True:
        # base condition
        if int(num) == compare_num:
            return print(count)
        # 입력된 값이 10보다 작을 때, 최초 0 주입
        result = (str(int(checknum[0])+int(checknum[1])))
        checknum.append(result[-1])
        checknum.pop(0)
        compare_num = int(checknum[0]+checknum[1])
        count+=1

get_cycle(n)