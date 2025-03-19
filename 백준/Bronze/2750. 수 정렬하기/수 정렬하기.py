T = int(input())  

num_list = []

def sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1):
            if int(lst[j]) > int(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

for i in range(T):
    num_list.append(input())

num_list = sort(num_list)

for i in range(T):
    print(num_list[i])