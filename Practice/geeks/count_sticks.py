__author__ = 'karthikb'

'''
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
'''
class Solution:
    def findMaxProfit(self,L,P,N):
        maxProfit= {L[i] : P[i] for i in range(0,len(P))}
        maxProfit[0] = 0
        for S in range(1,N+1):
            for i in range(0,S):
                if S >= L[i]:
                    diff = S - L[i]
                    #print "S:",S,"L:",L[i],"diff:",diff,"P[diff}","Summation:",P[i]+ maxProfit[diff],"other:",maxProfit[diff]
                    maxProfit[S]= max(maxProfit[diff] + P[i],maxProfit[S])
                    #print "maxProfit[S]",maxProfit[S]
        return maxProfit[N]

s = Solution()
L = [1, 2, 3, 4, 5, 6, 7, 8 ]
P = [1, 5, 8, 9, 10, 17, 17, 20 ]
print s.findMaxProfit(L,P,N=8)



