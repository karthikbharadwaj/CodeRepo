__author__ = 'karthikb'

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        ways = 0
        N = len(s)
        counts = 0
        if N:
            for i in range(0,N):
                count = self.countWays(i,N,s)
                if count == 2:
                    i+= 1
                counts += count
        return counts

    def countWays(self,i,N,A):
        count = 0
        if A[i] != '0':
            count = 1
            if i+1 < N and int(A[:i+1]) <= 26:
                count +=1
        return count

s = Solution()
print s.numDecodings('0')





