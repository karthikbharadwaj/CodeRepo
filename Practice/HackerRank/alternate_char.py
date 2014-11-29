__author__ = 'karthikb'

class Solution():
    def alternate_char(self, A):
        N = len(A)
        change = 0
        if N == 1:
            return 0
        i = 0
        while i <= N-2:
            if A[i] == A[i + 1]:
                change += 1
            i += 1
        return change
s = Solution()
print s.alternate_char('BBBBB')




