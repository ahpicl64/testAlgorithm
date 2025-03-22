try:
    while True:
        num = list(map(int,input().split()))
        num.sort()
        if num[0] == 0:
            None
        elif num[0]**2 + num[1]**2 == num[2]**2:
            print('right')
        elif num[0]**2 + num[1]**2 != num[2]**2:
            print('wrong')
        else:
            None
except:
    None