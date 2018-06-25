class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.use = float(val[0])
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.use > node.use:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    

f = open("allbp.data")
data = f.read()
lines = data.split('\n')

# print(len(lines[0].split(',')))
attr = len(lines[0].split(','))
count = [0]*attr
total = len(lines)

r = None

for line in lines:
    x = line.split(',')
    if len(x)<30:
        continue
    x.pop(-1)
    if r == None:
        r = Node(x)
    else:        
        #print(x)
        binary_insert(r,Node(x))

in_order_print(r)
