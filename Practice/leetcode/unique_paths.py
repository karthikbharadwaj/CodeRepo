__author__ = 'karthikb'
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        self._paths = {}
        return self._uniquePaths(m-1,n-1,0,0)

    def _uniquePaths(self,m,n,i,j):

        if (i,j) in self._paths:
            return self._paths[(i,j)]

        elif i == m and j == n:
            return 1
        elif i < m and j < n:
            paths = self._uniquePaths(m,n,i+1,j) + self._uniquePaths(m,n,i,j+1)
        elif i == m:
            paths = self._uniquePaths(m,n,i,j+1)
        else:
            paths = self._uniquePaths(m,n,i+1,j)
        self._paths[(i,j)] = paths
        return paths

s = Solution()
print s.uniquePaths(3,3)


