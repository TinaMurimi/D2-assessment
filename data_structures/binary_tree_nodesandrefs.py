class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = 33
        self.rightChild = None

    def insertLeft(self, newNode):
        """
         When there is no left child, simply add a node to the tree,
         else Insert a node and push the existing child down one
         level in the tree.
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self, tree):
        if tree is not None:
            postorder(tree.getLeftChild())
            postorder(tree.getRightChild())
            print(tree.getRootVal())

    def inorder(self, tree):
        if tree is not None:
            inorder(tree.getLeftChild())
            print(tree.getRootVal())
            inorder(tree.getRightChild())


r = BinaryTree('a')
print(r)
print(r.leftChild)
print(r.rightChild)

print()
print(r.getRootVal())
print(r.getLeftChild())

print('\nInsert left...')
r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
print(r.getRootVal())
print(r.leftChild)
print(r.leftChild.leftChild)
print(r.leftChild.rightChild)
print(r.rightChild)

print('\nInsert right...')
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())

print('\nReset root value...')
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
