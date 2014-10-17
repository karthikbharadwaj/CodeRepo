__author__ = 'karthikb'

class Solution:
    # @return an integer
    def reverse(self, x):

        assert isinstance(x,int)
        s = str(x)
        if x <0:
            s = s[1:]
            s = s[::-1]
            s = int(s)
            s = -1 * int(s)
        else:
            s = s[::-1]
            s = int(s)
        return s

s = Solution()
print s.reverse(-123)
