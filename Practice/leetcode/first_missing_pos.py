__author__ = 'karthikb'
class Solution:
    def firstMissingPositive(self, A):
        minPos = -1
        maxPos = 0
        sum = 0
        N = len(A)
        if N == 1:

        for item in A:
            if item > 0:
                minPos = min(minPos,item)
                maxPos = max(maxPos,item)
                sum = sum +item
        value =  N * (N+1)/2 - sum
        if value > 0:
            return value
        else:
            return maxPos + 1

s = Solution()
print s.firstMissingPositive([1])

