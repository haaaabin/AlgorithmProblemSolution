import sys

n = int(sys.stdin.readline())

tree = {}  #딕셔너리로 key = 부모, value = 자식

for i in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]   # root를 key로 left, right를 value   
    
def preorder(root):
    if root == '.':
        return
    else:
        print(root, end ='')
        preorder(tree[root][0])
        preorder(tree[root][1])
    
def inorder(root):
    if root == '.':
        return
    else:
        inorder(tree[root][0])
        print(root, end ='')
        inorder(tree[root][1])
        
def postorder(root):
    if root == '.':
        return
    else:
        postorder(tree[root][0])
        postorder(tree[root][1])       
        print(root, end ='')
        
preorder('A')
print()
inorder('A')
print()
postorder('A')