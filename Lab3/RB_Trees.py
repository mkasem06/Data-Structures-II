class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 # 1 for red, 0 for black

class RBTree:
    def __init__(self):
        self.NIL = Node("")
        self.NIL.color = 0 # 0 for black
        self.root = self.NIL

    def searchTree(self, key):
        node = self.root
        while node != self.NIL and key != node.val:
            if key < node.val:
                node = node.left
            else:
                node = node.right
        return node

    def getSize(self, node="START"):
        if node == "START":
            node = self.root
            
        if node == self.NIL:
            return 0
        return 1 + self.getSize(node.left) + self.getSize(node.right)

    def getHeight(self, node="START"):
        if node == "START":
            node = self.root
            
        if node == self.NIL:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    def getBlackHeight(self):
        node = self.root
        blackHeight = 0
        while node != self.NIL:
            if node.color == 0:
                blackHeight += 1
            node = node.left
        return blackHeight
    

    def leftRotate(self,x):
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent 
             
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self,y):
        x = y.left
        y.left = x.right
        
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent 
             
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
     new_node = Node(key)
     new_node.left = self.NIL
     new_node.right = self.NIL
     new_node.color = 1     # lazem tb2a red
     parent = None
     current = self.root

     while current != self.NIL:
        parent = current
        if new_node.val < current.val:
            current = current.left
        else:
            current = current.right

     new_node.parent = parent

     if parent is None:       # empty tree 
        self.root = new_node
     elif new_node.val < parent.val:
        parent.left = new_node
     else:
        parent.right = new_node

     self.fix_insert(new_node)
    
    
    def fix_insert(self, node):
        while node != self.root and node.parent.color == 1:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 1:   # uncle is red
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rightRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.leftRotate(node.parent.parent)
        self.root.color = 0
