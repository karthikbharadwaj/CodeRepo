__author__ = 'karthikb'


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = max_sum = - float('inf')
        value = 0
        for item in A:
            value += item
            if value > 0:
                max_so_far  < item:
        print max_so_far

        return max_sum

#A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
A = [-2, 4,1]
s = Solution()
print s.maxSubArray(A)
