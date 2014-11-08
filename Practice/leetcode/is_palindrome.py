__author__ = 'karthikb'

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        x = str(x)
        length = len(x)
        i,j = 0,length-1
        while i <=j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print s.isPalindrome(111111111112111)
