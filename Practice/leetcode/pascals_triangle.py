__author__ = 'karthikb'

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        a = {}
        a[(0,0)] = 1
        b = []
        for i in range(1,rowIndex + 1):
            for j in range(0,i+1):

                a[(i,j)] = a.get((i-1,j-1),0) + a.get((i-1,j),0)
                b.append(a[(i,j)])
        return b[rowIndex-1:]


s = Solution()
print s.getRow(2)
