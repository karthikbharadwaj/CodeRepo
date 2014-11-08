__author__ = 'karthikb'

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return 0
        diff = self.heightofLeftTree(root.left,0) - self.heightofRightTree(root.right,0)
        if -1 <= diff <= 1:
            return True
        return False

    def heightofLeftTree(self,root,value):
        if root is None:
            return value
        elif root.left:
            value = value + 1
            return self.heightofLeftTree(root.left,value)

    def heightofRightTree(self,root,value):

        if root is None:
            return value
        elif root.right:
            value = value + 1
            return self.heightofLeftTree(root.right,value)
