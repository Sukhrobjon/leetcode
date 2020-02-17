class Solution(object):
    # def isValidSudoku(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: bool
    #     """
    #     box = set()
    #     row = set()
    #     column = set()
    #     # row
    #     for i in range(len(board)):
    #         # column
    #         for j in range(len(board)):
    #             curr_num = board[i][j]
    #             # check if number is between 1 <= n <= 9
    #             if curr_num < 1 or curr_num > 9:
    #                 return False
    #             # 3X3 box check
    #             if i % 3 == 0 and j % 3 == 0:
    #                 for k in range(3):
    #                     pass

    
    # def check_row(self):
    #     pass
    
    # def check_column(self):
    #     pass

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


if __name__ == "__main__":
    obj = Solution()
    box = [
                    ["5", "3", "1"],
                    ["6", "2", "7"],
                    ["4", "9", "8"]
                ]

    check_box = obj.check_3_x_3_box(box)
    print(f"box: {check_box}")