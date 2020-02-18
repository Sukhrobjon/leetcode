class Solution(object):
    def is_valid_sudoku(self, board):
        """
        Check if the given sudoku board is valid
        """
        row = set()
        # column
        for i in range(len(board)):
            # row
            for j in range(len(board)):
                curr_row = board[i][j]
                # check if the element is number
                if curr_row != '.':
                    curr_row = int(curr_row)
                    print(f"column: {j}, number: {curr_row}")
                    # curr number is seen in the same column
                    if curr_row in row:
                        return False
                    else:
                        row.add(curr_row)
            # empty the row
            row = set()
        
        column = set()
        # row
        # j = 0
        for i in range(9):
            # column
            for j in range(9):
                curr_col = board[j][i]
                # check if the element is number
                if curr_col != '.':
                    curr_col = int(curr_col)
                    print(f"column: {i}, number: {curr_col}")
                    # curr number is seen in the same column
                    if curr_col in column:
                        print(f"column isnt right: {curr_col}")
                        return False
                    else:
                        column.add(curr_col)

            column = set()

        return True

    def check_3_x_3_box(self, box):
        seen = set()
        for i in range(3):
            for j in range(3):
                if box[i][j] != ".":
                    num = int(box[i][j])
                    if num in seen:
                        return False
                    seen.add(num)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # set for keeping track what is seen at that current row or column
        row = set()
        column = set()
        # row
        for i in range(len(board)):
            # column
            for j in range(len(board)):
                curr_row = board[i][j]
                curr_col = board[j][i]
                #=======================================#
                # CHECK FOR ROW
                if curr_row != '.':
                    curr_row = int(curr_row)
                    print(f"row: {j}, row_val: {curr_row}")
                    # curr number is seen in the same row
                    if curr_row in row:
                        print(f"row seen {curr_row}")
                        return False
                    else:
                        row.add(curr_row)
    
                #=======================================#
                # CHECK FOR COLUMN
                if curr_col != '.':
                    curr_col = int(curr_col)
                    print(f"column: {j}, col_val: {curr_col}")
                    # curr number is seen in the same column
                    if curr_col in column:
                        print(f"column seen {curr_col}")
                        return False
                    else:
                        column.add(curr_col)
                #=======================================#
                # CHECK FOR 3X3 box
                if i % 3 == 0 and j % 3 == 0:
                    print(i,j)
                    seen = set()
                    for m in range(3):
                        for n in range(3):
                            # set the counters for right position
                            r = m + i
                            c = n + j
                            if board[r][c] != ".":
                                num = int(board[r][c])
                                print(f"num: {num}, m: {r}, n: {c}")
                                if num in seen:
                                    return False
                                seen.add(num)
            row = set()
            column = set()
            
        return True
        

if __name__ == "__main__":
    obj = Solution()
    # for test 3x3 box 
    box = [
            ["5", "3", "1"],
            ["6", "2", "7"],
            ["4", "9", "8"]
        ]
    board = [
                ["5", "3", "2", ".", "7", "6", ".", ".", "."],
                ["6", "4", "7", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ]

    non_valid = [
                    [".", ".", ".", ".", "5", ".", ".", "1", "."],
                    [".", "4", ".", "3", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                    [".", ".", "2", ".", "7", ".", ".", ".", "."],
                    [".", "1", "5", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", "2", ".", ".", "."],
                    [".", "2", ".", "9", ".", ".", ".", ".", "."],
                    [".", ".", "4", ".", ".", ".", ".", ".", "."]
                ]
    check_box = obj.check_3_x_3_box(box)
    print(f"box: {check_box}")
    board_check = obj.isValidSudoku(non_valid)
    print(f"board: {board_check}")
