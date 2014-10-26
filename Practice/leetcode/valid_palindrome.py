__author__ = 'karthikb'
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = self.removeLetters(s)
        print s
        true_len = len(s)
        i,j = 0,true_len - 1
        while i <= j:
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                return False
        return True


    def removeLetters(self,s):
        new_string = ''
        for c in s:
            if c.isalnum():
                c = str.lower(c)
                new_string += c
        return new_string

s = Solution()
print s.isPalindrome('1a2')
