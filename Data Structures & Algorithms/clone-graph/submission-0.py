"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # A dictionary to map the original node -> cloned node
        # This acts as our 'visited' tracker as well
        copies = {}
        
        def dfs(curr_node):
            # If we already cloned this node, return the existing clone
            if curr_node in copies:
                return copies[curr_node]
            
            # Create a clone for the current node (without neighbors yet)
            clone = Node(curr_node.val)
            copies[curr_node] = clone
            
            # Recursively clone and populate the neighbors list
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)
