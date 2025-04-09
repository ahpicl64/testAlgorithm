n = int(input())

result = -1

for five in range(n//5, -1, -1):
    rest = n-5 * five # 5원의 개수만큼 나눴을 때 나머지
    if rest % 2 == 0:
        two = rest // 2
        result = two + five
        break

print(result)