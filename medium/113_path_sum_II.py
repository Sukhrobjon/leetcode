# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        all_path = []
        self.find_path(root, sum, all_path)
        # self.find_path_v2(root, sum, all_path)
        print(f"all_path: {all_path}")
        return all_path

    def find_path(self, node, sum, all_path, valid_path=None):
        # initialize the current path
        if valid_path is None:
            valid_path = []

        if node is None:
            return False, all_path

        valid_path.append(node.val)
        # reached leaf
        if node.left is None and node.right is None and sum == node.val:
            # copy the current path
            temp = valid_path[:]
            all_path.append(temp)

        self.find_path(node.left, sum-node.val, all_path, valid_path)
        self.find_path(node.right, sum-node.val, all_path, valid_path)

        valid_path.pop()

    def find_path_v2(self, node, target, all_path, valid_path=None):
        
        if valid_path is None:
            valid_path = []
        
        if node:
            if node.left is None and node.right is None and target == node.val:
                # copy the current path
                valid_path.append(node.val)
                all_path.append(valid_path)
            self.find_path_v2(node.left, target-node.val, all_path, valid_path+[node.val])
            self.find_path_v2(node.right, target-node.val, all_path, valid_path+[node.val])

if __name__ == "__main__":
    # build tree
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    # solution
    tree = Solution()
    result = tree.pathSum(root, 22)
    print(result)
