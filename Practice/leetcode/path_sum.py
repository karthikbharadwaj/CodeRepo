__author__ = 'karthikb'
# Problem: https://oj.leetcode.com/problems/path-sum/
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):

        if root:
            if root.left is None and root.right is None:
                if root.val == sum:
                    return True
                else:
                    return False

            else:
                return (self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val))
        else:
            return False
