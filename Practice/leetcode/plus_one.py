__author__ = 'karthikb'
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        length = len(digits)
        carry = 0
        s = [0] * length
        i = length - 1
        s[i],carry = self.detvalues(digits[i],1)
        i -= 1
        while i >= 0:
            s[i], carry = self.detvalues(digits[i],carry)
            i -= 1
        if carry:
            s.insert(0,carry)
        return s

    def detvalues(self,digit, value):
        sum = digit + value
        return sum % 10, sum / 10

s = Solution()
print s.plusOne([1,0])
