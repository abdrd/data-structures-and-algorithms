"""
    Binary tree implementation in Python programming language.

    In a binary tree a node can only have 2 child nodes at most.


        {5}  --> Root | Parent of the "Child of the root node"
       /  \     --> this is an edge of the tree
      /    \
     {4}   {6}  --> Child of the root node | has depth: 1
    /  \     \
   /    \     \
  {2}   {3}   {7}  --> Child node of the "Child of the root node" | has depth: 2
A leaf A leaf A leaf
            
Length of this tree is 2.

"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
    
    def __str__(self):
        return f"""<< {self.value} >>"""

    def insert(self, value):
        # no duplicates
        if self.value == value:
            return False

        # go to left
        if value < self.value:
            if self.left:
                return self.left.insert(value)

            self.left = Node(value)
            return True

        # go to right
        elif value > self.value:
            if self.right:
                return self.right.insert(value)

            self.right = Node(value)
            return True

    def find(self, value):
        if self.value == value:
            return True
        
        if value > self.value:
            if self.right:
                return self.right.find(value)

            return False

        elif value < self.value:
            if self.left:
                return self.left.find(value)
            return False
            
    def preorder(self):
        if self:
            print(str(self))

            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()

            print(str(self))
    
    def inorder(self):
        if self:
            if self.left:
                self.left.postorder()
                
            print(str(self))

            if self.right:
                self.right.postorder()

    def delete(self, value):
        pass


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        self.root = Node(value)
        return True
    
    def find(self, value):
        if self.root:
            return self.root.find(value)
        
        return False

    def preorder(self):
        print(" <PREORDER BEGIN> ")
        self.root.preorder()
        print(" <PREORDER END> ")

    def inorder(self):
        print(" <INORDER BEGIN> ")
        self.root.preorder()
        print(" <INORDER END> ")

    def postorder(self):
        print(" <POSTORDER BEGIN> ")
        self.root.preorder()
        print(" <POSTORDER END> ")

    # TODO delete method

bst = BinarySearchTree()
bst.insert(10)

print(bst.insert(15))
bst.insert(20)
bst.insert(50)
bst.insert(-12)

bst.preorder()
bst.postorder()
bst.inorder()

print(bst.find(15))
print(bst.find(-12))
print(bst.find(10))

print(bst.find(55))
