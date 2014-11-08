__author__ = 'karthikb'
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        ned_len = len(needle)
        hay_len = len(haystack)
        i = 0
        while i <= hay_len - ned_len:
            sub_str = haystack[i:i+ned_len]
            if needle == sub_str:
               return i
            i += 1
        return -1

s = Solution()
print s.strStr('abcd','cd')

