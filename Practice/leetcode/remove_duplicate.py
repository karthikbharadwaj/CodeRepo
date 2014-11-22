__author__ = 'karthikb'
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self,A):
        unique = {}
        count = 0
        length = len(A)
        for i in range(0,length-1):
            print i
            if A[i] ^ A[i+1] ==0:
               A.pop(i)
               i = i + 1
        return A

s = Solution()
print s.removeDuplicates([2,2,4])

