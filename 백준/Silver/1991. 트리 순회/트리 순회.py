tree = {}

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

# 전위 순회   
def preorder(node):
    if node != '.':
        print(node.item, end = "")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
    

# 중위 순회
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    if node != '.':
        print(node.item, end = "")
    if node.right != '.':
        inorder(tree[node.right])


# 후위 순회
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    if node != '.':
        print(node.item, end = "")


n = int(input())
for _ in range(n):
    item, left, right = map(str,input().split())
    tree[item] = Node(item,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])