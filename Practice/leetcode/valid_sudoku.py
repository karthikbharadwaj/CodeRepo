__author__ = 'karthikb'
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):

        vert_dict = {}
        hor_dict = {}
        box_start = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        a = board
        for i in range(0,8):

            for j in range(0,8):
                if a[i][j] != '.':
                    if a[i][j] not in hor_dict:
                        hor_dict[a[i][j]] = 1
                    else:
                        print i,j
                        return False
                if a[j][i] != '.':
                    if a[j][i] not in hor_dict:
                        vert_dict[a[i][j]] = 1
                    else:
                        print "vert pos",a[j][i]
                        print vert_dict
                        return False
        return True

s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
