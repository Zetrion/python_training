class TreeNodes:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
  
root = TreeNodes(1)        
A = TreeNodes(2)
B = TreeNodes(3)
C = TreeNodes(4)    
D = TreeNodes(5)
E = TreeNodes(6)
F = TreeNodes(7)        

root.left = A
root.right = B  
A.left = C
A.right = D 
B.left = E
B.right = F

def pre_order_traversal(node):
    if node is not None:
        print(node.data, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

pre_order_traversal(root)

def in_order_traversal(node):   
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=' ')
        in_order_traversal(node.right)
        
in_order_traversal(root)    

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=' ')
        
        
post_order_traversal(root)                