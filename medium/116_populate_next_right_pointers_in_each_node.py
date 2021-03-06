"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None
        return self.connect_right_pointers(root)

    def connect_right_pointers(self, root):
        """
        """
        node = root
        level = 0
        # start off with root
        queue = [(node, level)]
        while queue:
            node, p_level = queue.pop(0)
            if node.left:
                queue.append((node.left, p_level+1))
            if node.right:
                queue.append((node.right, p_level+1))

            # check if queue is not empty
            if queue:
                # peek the top, if the levels are the same then we can connect
                next_node, n_level = queue[0]
                # if their level is equal then we can connect
                if p_level == n_level:
                    node.next = next_node
                # if level is not equal
                else:
                    node.next = None
            # else we pop the last item we just assign the next pointer to none
            else:
                node.next = None
        return root

    def connect_no_extra_space(self, root):
        """
            Connects the tree nodes with right side of the node, if exists
            using no extra memory
            credit https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37461/Java-solution-with-O(1)-memory%2B-O(n)-time
        """
        # curr level
        level = root

        while level is not None:
            # curr node
            node = level
            
            while node is not None:
                # if left node and right exists
                if node.left:
                    node.left.next = node.right
                # if only left node
                if node.right is not None and node.next is not None:
                    node.right.next = node.next.left

            node = node.next
        
        # step down one level
        level = level.left
