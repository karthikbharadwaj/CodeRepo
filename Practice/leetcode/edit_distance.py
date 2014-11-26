__author__ = 'karthikb'

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        min_dict = dict({(-1,-1):0,(0,-1):0,(-1,0):0})
        #min_dict[(-1,-1)] = 0
        m, n = len(word1),len(word2)
        for i in range(1,m+1):
            min_dict[(i,0)] = i
        for j in range(0,n+1):
            min_dict[(0,j)] = j
        #print min_dict
        for i in range(1,m+1):
            for j in range(1,n+1):
                diff = self.diff(word1[i-1],word2[j-1])
                min_dict[(i,j)] = min(min_dict[(i-1,j-1)] + diff,min_dict[(i-1,j)] + 1,min_dict[(i,j-1)] + 1)

        return min_dict[(m,n)]

    def diff(self,char1,char2):
        if char1 == char2:
           return 0
        return 1

s = Solution()
print s.minDistance("","e")


