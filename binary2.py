import random

ran = []
#create random number of arrays that contains 1 to 100
for i in range(0,10):
    ran.append(random.randint(1,10))
print(ran)

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None 

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        elif val == self.root:
            return self.root
        else:
            self.insertNode(val, self.root)

    def insertNode(self,val,node):
        if val < node.val:
            if node.left == None:
                node.left = Node(val)
            elif val == node.left:
                return node.left
            else:
               self.insertNode(val, node.left)
        else:
            if node.right == None:
                node.right = Node(val)
            elif val == node.right:
                return node.right
            else:
               self.insertNode(val, node.right)
#this variable is gonna be used to make space
def maxDepth(node):
    if node == None:
        return 0
    else :
        ldepth = maxDepth(node.left)
        rdepth = maxDepth(node.right)

        if (ldepth>rdepth):
            return ldepth +1
        else :
            return rdepth +1
#level order tranversal
def printDepths(tree):
    Q = []
    mark = Node(10000)
    low = 1
    high = maxDepth(tree.root)
    level = 1
    Q.append(tree.root)
    Q.append(mark)

    for i in range(0,high+1):
        print(" ",end="")
    while(len(Q) > 0):
        n = Q[0]
        Q.pop(0)

        if n == mark:
            print("")
            for i in range(0,high-level):
                print(" ",end="")
            level += 1
            if len(Q) == 0 or level > high:
                break
            Q.append(mark)
            continue
        if level >= low:
            if n.val != None:
                if level == 1 or Q[0] == mark:
                    print ("({})".format(n.val),end="")
                else:
                    print ("({}),".format(n.val),end="")
            else:
                continue

        if n.left != None:
            Q.append(n.left)
        if n.right != None:
            Q.append(n.right)

#use to create random binary tree
tree = Tree()
for i in range(0,len(ran)):
    tree.add(ran[i])
#put any binary tree here
printDepths(tree)





