"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        # perform level order traversal
        largest = float('-inf')
        values = []
        level = 0
        queue = [(root, level)]

        while queue:
            node, p_level = queue.pop(0)

            # add the left and right
            if node.left:
                queue.append((node.left, p_level+1))
            if node.right:
                queue.append((node.right, p_level+1))

            # before comparing make sure we are comparing the nodes on the same level

            if node.val > largest:
                largest = node.val
            # now check if we need to add the largest val
            # if curr node is last node in this level or queue is empty
            if len(queue) == 0:
                values.append(largest)
                # reset the largest
                largest = float('-inf')
            # then we know there is at least one element in queue
            else:
                front = queue[0][1]
                # check if this node is the last element in the node
                if front != p_level:
                    values.append(largest)
                    # reset the largest
                    largest = float('-inf')

        return values
