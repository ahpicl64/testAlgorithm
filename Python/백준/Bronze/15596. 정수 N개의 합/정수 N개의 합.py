def solve(a):
    length = len (a)
    ans = 0
    for i in range(length):
        ans += int(a[i])
    return ans