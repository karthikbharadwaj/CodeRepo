__author__ = 'karthikb'

class Solution:
# @param s, a string
# @param dict, a set of string
# @return a boolean
    def wordBreak(self, s, dict):
        max_present = {}
        org_word = s
        i = len(s)-1
        while i >=0 and s:
            #print "checking for",i,s[:i]
            if s[:i] in dict:
                #print "matching",s[:i]
                s = s[i:]
                #print "now s",s
                i = len(s) + 1
                #print "i becomes",i,s[:i]
            i = i - 1
        if s == '' and i ==0:
            return True
        else:
            return False







s = Solution()
print s.wordBreak("aaaaaaa", ["aaaa","aaa"])

