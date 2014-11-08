__author__ = 'karthikb'
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red = blue = white = []
        #red,blue,white = [],[],[]
        for item in A:
            if item == 0:
                red.append(item)
            elif item == 1:
                white.append(item)
            else:
                blue.append(item)
        return red + white + blue

s = Solution()
print s.sortColors([1,0])

