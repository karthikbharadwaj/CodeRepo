__author__ = 'karthikb'
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
        elif root.left is not None:
            return 1 + self.minDepth(root.left)
        elif root.right is not None:
            return 1 + self.minDepth(root.right)
        else:
            return 1
