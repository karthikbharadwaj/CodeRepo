__author__ = 'karthikb'
'''
Problem statement :http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
'''

class Solution:
    def findmaxZigZag(self,A):
        maxZigZag = {}
        N = len(A)
        if N >1:
            maxZigZag[0] = 1

        if N >=2:
            maxZigZag[0] = 2
            diff = A[0] - A[1]
            for i in range(1,N-1):
                if (diff >0 and A[i]< A[i+1]) or (diff <0 and A[i] > A[i+1]):
                    maxZigZag[i]= maxZigZag[i-1] + 1
                    diff = A[i] - A[i+1]
                else:
                    maxZigZag[i] = maxZigZag[i-1]
        return maxZigZag[N-2]

s = Solution()
print s.findmaxZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
249, 22, 176, 279, 23, 22, 617, 462, 459, 244])
