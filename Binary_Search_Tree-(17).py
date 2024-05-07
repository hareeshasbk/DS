# Program :17
# Python program to implement Binary Search Tree

class Node:
    def __init__(self,key):
        self.left= None
        self.data=key
        self.right=None
        
def insert(node,key):
        if node is None:
            return Node(key)
        
        if key< node.data:
            node.left=insert(node.left,key)
        else:
            node.right=insert(node.right,key)
        return node
    
def inorder(root):
        if root is not None:
            inorder(root.left)
            print(str(root.data)+" ")
            inorder(root.right)

def exists(node,val):
        if val == node.data:
            return True

        if val<node.data:
            if node.left == None:
                return False
            return exists(node.left,val)

        if node.right == None:
            return False
        return exists( node.right,val)

root= None

root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder =")
inorder(root)


x=int(input("Enter value you want to search:"))
if (exists(root,x)):
    print("Found")
else:
    print("Not Found")

