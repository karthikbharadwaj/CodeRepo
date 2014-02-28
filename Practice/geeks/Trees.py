'''
Package for tree problems
'''


class TreeNode():

    def __init__(self, data):

        self._data = data
        self._left = None
        self._right = None

class Tree():

    def __init__(self, data=None):

        self._root = None


    def _add_node(self,root,data):

        new_node = TreeNode(data)
        if self._root:

            self._root = new_node
        elif data > self._root.data:

            self._add_node(self.
treenode = TreeNode(10)
