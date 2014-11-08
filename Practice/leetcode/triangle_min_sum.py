__author__ = 'karthikb'

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        min_sum = {}
        length = len(triangle)
        for i in range(length -1,-1,-1):
            for j in range(0,len(triangle[i])):
                min_sum[(i,j)] = min(min_sum.get((i+1,j),0) , min_sum.get((i+1,j+1),0)) + triangle[i][j]

        return min_sum[(0,0)]




s = Solution()
a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print s.minimumTotal(a)