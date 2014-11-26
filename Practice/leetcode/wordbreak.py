__author__ = 'karthikb'

class Solution:
# @param s, a string
# @param dict, a set of string
# @return a boolean
    word_dict = {}
    index_dict = {}
    def wordBreak(self, s,dict):
        word_dict = {word: 1 for word in dict}
        start, end = 0, len(s)
        return self.dp_word_break(s, start, end ,word_dict)

    def dp_word_break(self,s, start, end , word_dict):
        if (start, end) in self.index_dict:
            return self.index_dict[(start, end)]
        elif start > end:
            self.index_dict[(start,end)] = 0
        elif s[start:end] in self.word_dict:
            print "Comes here"
            self.index_dict[(start,end)] = 1
        else:
            self.index_dict[(start, end)] = max(self.dp_word_break(s,start + 1,end, word_dict),self.dp_word_break(s,start, end - 1, word_dict))

        return self.index_dict[(start, end)]


s = Solution()
print s.wordBreak("a", ["aaaa","aaa","a"])

