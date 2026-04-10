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