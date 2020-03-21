"""
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
            Runtime: O(n) because we need to visit each node
            Space complexity: O()
        """
        # queue for regular level order
        queue = []
        # keep the zigzag order for coressponding levels(odd levels)
        stack = []
        level = 0
        zigzag_order = []
        queue.append((root, level))

        while queue:
            # pop the front of the queue
            node, level = queue.pop(0)

            # add its children and child's level
            if node.left:
                queue.append((node.left, level+1))

            if node.right:
                queue.append((node.left, level+1))

            # if level of current node is odd that means we need to add it to
            # result in reversed order
            front_level = queue[0][1]
            # if the next node's level is even now we need to empty out the stack and put it
            # into output result
            if front_level % 2 == 0:
                zigzag_order[level] = []
                while len(stack) != 0:
                    # pop the top of the stack
                    node = stack.pop()
                    zigzag_order[level].append(node.val)
            if level % 2 != 0:
                # we put them in stack
                stack.append(node)
            # otherwise we perform the regular order
            else:
