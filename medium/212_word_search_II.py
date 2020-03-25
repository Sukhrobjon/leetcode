class Solution:
    # def findWords(self, board, words):
    #     visited = [[False for j in range(
    #         len(board[0]))] for i in range(len(board))]
    #     exist_words = []
    #     for word in words:
    #         exist = self.exist(board, word, visited)
    #         print("word:", word)
    #         if exist:
    #             print("word is in board:", word)
    #             exist_words.append(word)
    #         print(visited)
    #     return exist_words

    def exist(self, board, words):

        all_words = []
        visited = [[False for j in range(
                    len(board[0]))] for i in range(len(board))]
        for word in words:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    match = self.dfs(board, word, row, col, 0, visited)
                    # match = self.dfs_no_extra_memory(board, word, row, col, 0)
                    
                    if match:
                        all_words.append(word)
                        print(visited)

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



obj = Solution()
board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]
current_word = "tea"
# is_exist = obj.exist(board, current_word,)
all_words = obj.exist(board, words)
print(all_words)
# print(f'{current_word} => {is_exist}')
