__author__ = 'karthikb'
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    board_dict = {}
    location_dict = {}
    def exist(self, board, word):
        new_board,board_positions = self.process_board(board)
        self.get_neighbours(board)

    def process_board(self, board):
        rows = len(board)
        new_board = []
        neighbours = {}
        board_positions = {}
        for row_index in range(rows):
            row_string = board[row_index][0]
            new_board.append(list(row_string))
            row_len = len(row_string)
            for col_index in range(row_len):
                if col_index + 1 < row_len:
                    neighbours[row_index][col_index]
                board_positions.setdefault(row_string[col_index],[]).append((row_index,col_index))
        return new_board,board_positions

    def get_neighbours(self,board):
        for row_index in range(len(board)):
            row = board[row_index]
            for col_index in range(len(row)):
                col_index

        return







board = [["ABCE"],["SFCS"],["ADEE"]]
s = Solution()
s.exist(board,"SEE")



