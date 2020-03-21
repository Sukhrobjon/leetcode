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
    def zigzagLevelOrder(self, root: TreeNode):
        """
            Runtime: O(n) because we need to visit each node
            Space complexity: O()
        """
        # queue for regular level order

        if not root:
            return []
        queue = []
        # keep the zigzag order for coressponding levels(odd levels)
        stack = []
        level = 0
        zigzag_order = []
        queue.append((root, level))

        while queue:
            print("queue after child:", queue)
            # pop the front of the queue
            node, p_level = queue.pop(0)

            # add its children and child's level
            if node.left:
                queue.append((node.left, p_level+1))

            if node.right:
                queue.append((node.right, p_level+1))
            print("queue after child:", queue)
            # if level of current node is odd that means we need to add it to
            # result in reversed order
            # if stack is not empty and the current node is the last item on this level
            # we need to pop all the items in the stack and put them in the output list
            if p_level % 2 != 0:
                # we put them in stack
                stack.append(node)
                print("node in stack", node.val)
                print(stack)
                # we need to check if this the last node at this level or
                # it is the last level in the tree
                # reference -> queue[0][1] = next_node_level
                if (len(queue) > 0 and p_level != queue[0][1]) or len(queue) == 0:
                    # create spot for nodes in zigzag order
                    zigzag_order.append([stack.pop().val])
                    # pop all nodes from stack
                    while stack:
                        node = stack.pop()
                        zigzag_order[p_level].append(node.val)
            # otherwise we perform the regular order
            else:
                # we need to check if it is needed to create new position for this level
                # nodes at that level has already been added(at least one of them added)
                if len(zigzag_order) == p_level + 1:
                    zigzag_order[p_level].append(node.val)
                # nodes at this level never been added to output list
                elif len(zigzag_order) < p_level + 1:
                    zigzag_order.append([node.val])

        return zigzag_order



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(13)
root.right.left.left = TreeNode(8)
obj = Solution()
result = obj.zigzagLevelOrder(root)
print(result)
