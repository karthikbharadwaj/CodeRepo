__author__ = 'karthikb'

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if A is None or len(A)<1:
            return 0
        else:
            return sum(A) % 3

s = Solution()
print s.singleNumber([2,2,3,2])
