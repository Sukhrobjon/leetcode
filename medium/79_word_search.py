class Solution:
    def exist(self, board, word):
        visited = [[False for j in range(
            len(board[0]))] for i in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                # match = self.dfs(board, word, row, col, 0, visited)
                match = self.dfs_no_extra_memory(board, word, row, col, 0)
                if match:
                    return True
        
        return False
    
    def dfs(self, board, word, row, col, index, visited):
        
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        # if char is unmatch or that elem was visited
        if board[row][col] != word[index] or visited[row][col]:
            # print(visited)
            return False

        # otherwise we have a match
        char = board[row][col]
        visited[row][col] = True

        up = self.dfs(board, word, row-1, col, index+1, visited)
        down = self.dfs(board, word, row+1, col, index+1, visited)
        right = self.dfs(board, word, row, col+1, index+1, visited)
        left = self.dfs(board, word, row, col-1, index+1, visited)

        if up or down or right or left:
            print(char)
            return True
        # back tracking if we get this point
        # board[row][col] = "#"
        visited[row][col] = False

        return False

    def dfs_no_extra_memory(self, board, word, row, col, index):
        
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        # if char is unmatch or that elem was visited
        if board[row][col] != word[index]:
            # print(visited)
            return False

        # otherwise we have a match
        char = board[row][col]
        board[row][col] = " "

        up = self.dfs_no_extra_memory(board, word, row-1, col, index+1)
        down = self.dfs_no_extra_memory(board, word, row+1, col, index+1)
        right = self.dfs_no_extra_memory(board, word, row, col+1, index+1)
        left = self.dfs_no_extra_memory(board, word, row, col-1, index+1)

        if up or down or right or left:
            print(char)
            return True
        # back tracking if we get this point
        board[row][col] = char
        # visited[row][col] = False

        return False

obj = Solution()
board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
word = 'SEE'
result = obj.exist(board, word)
print(result)




'''


    def exist_v2(self, board, word):
        """
        Given a 2D board and a word, find if the word exists in the grid.
        The word can be constructed from letters of sequentially adjacent cell,
        where "adjacent" cells are those horizontally or vertically neighboring
        The same letter cell may not be used more than once
        """
        # an array to mark the visited cell(indexes)
        
        # queue to keep track of the order
        queue = []
        # index for word we are looking for
        index = 0
        to_word = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                print("row:", row)
                print("col:", col)
                print("forming word: ", to_word)
                # check if the element was visited
                if index == len(word):
                    return True
                if not visited[row][col]:
                    # put it into visited
                    visited[row][col] = True
                    # check if letter matches with word letter
                    if board[row][col] == word[index]:
                        to_word.append(board[row][col])
                        index += 1
                    # check row wise
                    else:
                        # bound check
                        if row >= len(board):
                            continue
                        if not visited[col][row]:
                            visited[col][row] = True
                            # check if letter matches with word letter
                            if board[col][row] == word[index]:
                                to_word.append(board[row][col])
                                index += 1
        return False
'''
