# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        all_path = []
        n_sum = 0
        path_sum = self.root_to_leaf(root, n_sum, all_path.append)
        print(f"all_paths:", all_path, n_sum)
        print(sum(all_path))
        return 1026

    def root_to_leaf(self, node, curr_sum, all_path, path=None):
        """
        Helper function to traverse the tree and calculate the path
        sum
        """
        if path is None:
            path = []
    
        if node is None:
            # sum of all
            print(f"when it hit the none: allpath: {(all_path)}, sum: {curr_sum}, path: {path}")
            return all_path

        path.append(node.val)
        # go the left
        if node.left is None and node.right is None:
            # calculate the sum
            path_val = int("".join(str(num) for num in path))
            all_path(path_val)
            print('curr path:', path_val)
            curr_sum += path_val
            print("curr_sum:", curr_sum)

        self.root_to_leaf(node.left, curr_sum, all_path, path)
        self.root_to_leaf(node.right, curr_sum, all_path, path)
        path.pop()



if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)


    tree = Solution()
    result = tree.sumNumbers(root)
    print(result)
