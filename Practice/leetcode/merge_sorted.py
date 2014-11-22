__author__ = 'karthikb'

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        #Expanding A
        for k in range(m,m+n):
            A.append(0)
        i,j,k = m - 1, n - 1, m + n - 1
        while i >=0 and j>=0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        while j >=0:
            A[k] = B[j]
            j -= 1
            k -= 1
        return A




s = Solution()
print s.merge([2,3],2,[1,8,9],3)
#print s.merge([-50,-49,-49,-48,-47,-45,-43,-41,-41,-41,-40,-40,-39,-39,-38,-37,-37,-36,-36,-35,-35,-33,-33,-32,-31,-31,-30,-30,-29,-28,-25,-24,-21,-19,-18,-18,-14,-13,-10,-10,-9,-9,-9,-6,-6,-5,-1,1,7,10,10,11,13,14,14,15,20,21,21,22,23,25,26,27,30,30,31,32,33,35,36,38,40,40,41,41,42,44,46,46,46,46,46,47,48],85,[33],1)

