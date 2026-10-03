"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None

        nodeMap = {}
        cur = head

        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = nodeMap[cur]

            copy.next = nodeMap.get(cur.next)
            copy.random = nodeMap.get(cur.random)

            cur = cur.next
        
        return nodeMap[head]