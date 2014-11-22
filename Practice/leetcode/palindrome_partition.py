__author__ = 'karthikb'
class Solution:
    # @param s, a string
    # @return a list of lists of string
    part_dict = {}
    def partition(self, s):
        i,j = 0,len(s)-1
        return self.computePartition(s,i,j)

    def computePartition(self,s,i,j):


s = Solution()
print s.partition("aabb")

