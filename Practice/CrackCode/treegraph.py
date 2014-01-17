__author__ = 'karthikb'

'''Crack the coding interview problems tree and Graphs'''

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.data)

root = Tree(4)
print root.data


def pre_order(root):
    if root is None:
        return root

    print root.data
    pre_order(root.left)
    pre_order(root.right)

def post_order(self,root):

    if root is None:
        return root
    self.post_order(root.left)
    self.post_order(root.right)
    print root.data

def in_order(self,root):

    if root is None:
        return root

    self.in_order(root.left)
    print root.data
    self.in_order(root.right)




Tree(root,3,5)




#btree.in_order(root)
def min_depth(root):

    if root is None:
        return 0

    return 1+ min(min_depth(root.left),min_depth(root.left))

def max_depth(root):

    if root is None:
        return 0

    return 1+ max(min_depth(root.left),min_depth(root.left))

#print min_depth(root)
#print max_depth(root)
def balanced_check(root):

    return max_depth(root) - min_depth(root) <=1










