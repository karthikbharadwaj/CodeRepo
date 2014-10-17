__author__ = 'karthikb'

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        str_len = len(s)
        i = 0
        max_matching = self.max_matching_string(s,dict)
        if max_matching:
            new_index = len(max_matching)
            i += new_index
            if i == len(s):
                return True
            else:
                return self.wordBreak(s[i:],dict)
        else:
            return False

    def max_matching_string(self,s,dict):
        matched_string = []
        max_len = 0
        max_item = None
        for item in dict:
            if item in s:
                if max_len < len(item):
                    max_len = len(item)
                    max_item = item
        return max_item








s = Solution()
print s.wordBreak("aaaaaaa", ["aaaa","aaa"])

