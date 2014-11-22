__author__ = 'karthikb'

class Solution:
    def minCut(self, s):
        N = len(s)
        return self._palin_partition(s,0,N)

    def _palin_partition(self,S,i,j):
        N = len(S)
        minPal = {0:float('inf')}
        for k in range(1,N+1):
            minPal[k] = min(self.isPalindrome(S[:k])+ 1,self.isPalindrome(S[k:]))
        return minPal[N]

    def isPalindrome(self,S):
        i,j = 0,len(S)-1
        while i <j:
            if S[i] != S[j]:
                return 1
            i +=1
            j -= 1
        return 0



s = Solution()
print s.minCut("aaaaba")

