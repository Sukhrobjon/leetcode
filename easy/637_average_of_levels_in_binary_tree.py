"""
Given a non-empty binary tree, return the average value of the nodes on each
level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if not root:
            return []

        averages = self.level_order_v2(root)

        return averages

    def level_order_v2(self, root):
        """
            We perform bfs to traverse the tree, and calculate
            each levels sum
        """
        queue = deque([root])
        average_of_levels = []
        curr_level = []
        while len(queue) != 0:
            # for each level
            curr_level = []
            for i in range(len(queue)):
                # pop the value

                node = queue.popleft()
                curr_level.append(node.val)
                # the we add the children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = sum(curr_level) / len(curr_level)
            average_of_levels.append(average)

        return average_of_levels
