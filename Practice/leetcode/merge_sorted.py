__author__ = 'karthikb'

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        sorted_array = []
        if m>0 and n > 0:
            i,j = 0,0
            while i < m and j < n:
                if A[i] < B[j]:
                    sorted_array.append(A[i])
                    i += 1
                else:
                    sorted_array.append(B[j])
                    j += 1
            if j == n:
                sorted_array.extend(A[i:])
            else:
                sorted_array.extend(B[j:])
            #assigning back to A
            A = sorted_array
        elif B:
            A = B
        return

    def check_edges(self, A, m, B, n):
        if A[0] > B[0] and A[m - 1] > B[0]:
            return A.extend(B)
        elif B[0] > A[0] and B[n - 1] > A[0]:
            return B.extend(A)
        else:
            return 0

s = Solution()
print s.merge([],0,[1],1)
#print s.merge([-50,-49,-49,-48,-47,-45,-43,-41,-41,-41,-40,-40,-39,-39,-38,-37,-37,-36,-36,-35,-35,-33,-33,-32,-31,-31,-30,-30,-29,-28,-25,-24,-21,-19,-18,-18,-14,-13,-10,-10,-9,-9,-9,-6,-6,-5,-1,1,7,10,10,11,13,14,14,15,20,21,21,22,23,25,26,27,30,30,31,32,33,35,36,38,40,40,41,41,42,44,46,46,46,46,46,47,48],85,[33],1)

