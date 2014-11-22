__author__ = 'karthikb'
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):

        negFlag = 0
        if x <0:
            negFlag = 1
        i = 0
        while i**2 <= x:
            i += 1
        result = i - 1
        if negFlag:
            result = -1 * result
        return result

s = Solution()
print s.sqrt(1708088682)

