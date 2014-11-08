__author__ = 'karthikb'

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        subsets = []
        S = sorted(S)
        #S = sorted(S,reverse=True)
        count = 0
        i = 1
        for i in range(0,2 **len(S)):
            values = []
            for j in range(0,len(S)):
                t= 1<<j
                if i & (t):
                    values.append(S[j])
            subsets.append(values)
        return subsets

s = Solution()
print s.subsets([4,1,0])
