__author__ = 'karthikb'

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while elem in A:
            A.remove(elem)
        return len(A)

s = Solution()
print s.removeElement([3,3,1],3)
