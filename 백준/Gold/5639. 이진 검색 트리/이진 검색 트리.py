import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def print_postorder(lower, upper, idx):
    if idx[0] >= len(preorder):
        return
    if not (lower < preorder[idx[0]] < upper):
        return

    root = preorder[idx[0]]
    idx[0] += 1

    print_postorder(lower, root, idx)
    print_postorder(root, upper, idx)
    print(root)

idx = [0]
print_postorder(-10**9, 10**9, idx)