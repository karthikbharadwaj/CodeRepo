__author__ = 'karthikb'

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add_item(self,root,item):
        new_node = TreeNode(item)
        if root is None:
            root = new_node
        elif root.val >= item:
            self.add_item(root.left,item)
        else:
            self.add_item(root.right,item)

    def print_tree(self):
        if self.root:
            print self.root.val
        elif self.root.left:




t = Tree()
t.add_item(t.root,10)
t.print_tree(t.root)


