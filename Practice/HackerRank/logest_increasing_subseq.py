__author__ = 'karthikb'

class Solution:

    def longest_subseq(self, A):
        N = len(A)
        if N == 0:
            return 0
        current_max =  A[0]
        max_J = 0
        L = {0:1}
        for i in range(0,N):
            max_I = 1
            for j in range(0,i):
                max_count = L[j]
                if A[i] > A[j]:
                    max_I = max(max_I,max_count + 1)
            L[i] = max_I
        return L[N-1]


#A = [2,7,4,3,8]
s = Solution()
print s.longest_subseq(A)


