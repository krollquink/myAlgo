import random



ran = []
#create random number of arrays that contains 1 to 100
for i in range(0,10):
    ran.append(random.randint(1,10))

print(ran)

    def create_tree(self):
        if (array==[]):
            return None
        mytree = Tree()
        mytree.root = Node()
        mytree.root.value = array[0]

#class Node:
#    def __init__(self,val):
#        self.left = None
#        self.right = None
#        self.value = val
#
#class Tree:
#    def __init__(self,value):
#        self.root = value
#        self.left = None
#        self.right = None
#
#    def insertLeft(self,value)
#        if value < self.root:
#            if self.left == None
#                self.left = Tree(value)
#            else:
#                tree = Tree(value)
#                tree.left = self.left
#                self.left = tree
#        else:
#            insertRight(value)
#
#    def insertRight(self,value)
#        if value > self.root:
#            if self.right == None
#                self.right = Tree(value)
#            else:
#                tree = Tree(value)
#                tree.right = self.right
#                self.right = tree
#        else:
#            insertLeft(value)
#
#
#    def create_tree(self,array)
#        tree = Tree(array[0])
#        for i in range(1,len(array)):
#            if array[i] < tree.root 
#                insertLeft(array[i])
#            else:
#                insertRight(array[i])
#        
#
#
#
#
#            if array[i] < mytree.root.value:
#                mytree.root.left = Node()
#                mytree.root.left.value = array[i]
#            else:
#                mytree.root.right = Node()
#                mytree.root.right.value = array[i]
# 
    



create_tree(ran)
