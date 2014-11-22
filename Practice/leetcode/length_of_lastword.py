__author__ = 'karthikb'


class Solution:
    # @param s, a string
    # @return an integer
    def get_last_words(self,s):


        length = len(s)
        words = []
        word = ''
        letterCounter = 0
        i = length-1
        while i >= 0:
            if ord('a') <= ord(s[i]) <= ord('z') or ord('A') <= ord(s[i]) <= ord('Z'):
                word = s[i] + word
                letterCounter += 1
            elif s[i] == ' ' and letterCounter:
                words.append(word)
                word = ''
                return words
            i -= 1
        if word != '':
            words.append(word)
        return words

    def lengthOfLastWord(self, s):
        words = self.get_last_words(s)
        print words
        total_words = len(words)
        if total_words >0:
            result = len(words[total_words - 1])
            return result
        else:
            return 0

s = Solution()
print s.lengthOfLastWord(" ")
