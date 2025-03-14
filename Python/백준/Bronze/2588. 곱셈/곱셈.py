a = int(input())
b = input()

hundred = a*int(b[0])
ten = a*int(b[1])
one = a*int(b[2])
result = hundred*100 + ten*10 + one

print(one)
print(ten)
print(hundred)
print(result)