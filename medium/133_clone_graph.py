"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its
neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        clone_node = Node(node.val)
        visited = {node: clone_node}
        queue = deque([node])

        while queue:
            node = queue.popleft()
            # print("node:", node.val)
            for neighbor in node.neighbors:

                if neighbor not in visited:
                    # make a clone node
                    # print("neighbor:", neighbor.val)
                    neighbor_clone = Node(neighbor.val)
                    visited[neighbor] = neighbor_clone
                    visited[node].neighbors.append(neighbor_clone)
                    queue.append(neighbor)

                # if it is visited we need to append the cloned neighbor
                else:
                    # clone of the neighbor
                    clone_n = visited[neighbor]
                    visited[node].neighbors.append(clone_n)

        return clone_node
