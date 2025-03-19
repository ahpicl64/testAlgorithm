import sys
count_recursion = 0

def recursion(s, l, r):
    global count_recursion
    count_recursion+=1

    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        # count_is_palidrome+=1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


T = int(sys.stdin.readline().strip('\n'))

for i in range(T):
    s = sys.stdin.readline().strip('\n')
    print(F"{isPalindrome(s)} {count_recursion}")
    count_recursion = 0