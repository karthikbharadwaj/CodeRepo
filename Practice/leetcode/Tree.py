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
        if self.root is None:
            self.root = new_node
        elif self.root.val >= item:
            self.add_item(root.left)


