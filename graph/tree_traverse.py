### Tree Traverse ###
# Pre-order, In-order, Post-order

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

# input data에 따라 tree 만들기
with open("tree_traverse.txt", "r") as f:
    n = int(f.readline().strip())
    tree = {}
    for i in range(n):
        data, left, right = f.readline().split()
        if left == "None":
            left = None
        if right == "None":
            right = None
        tree[data] = Node(data, left, right)

# 트리 순회
print("Pre-order: ", end=' ')
pre_order(tree['A'])    # A B D E C F G
print()
print("In-order: ", end=' ')
in_order(tree['A'])     # D B E A F C G
print()
print("Post-order: ", end=' ')
post_order(tree['A'])   # D E B F G C A
print()