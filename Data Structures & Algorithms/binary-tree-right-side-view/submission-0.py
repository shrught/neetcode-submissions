# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        q = deque()
        result = []

        def bfs(node):
            if not node:
                return
            q.append(node)
            depth = 1
            
            while(q):
                sz = len(q)
                for i in range(sz):
                    cur = q.popleft()
                    if i == sz - 1:
                        result.append(cur.val)

                    if cur.left is not None:
                        q.append(cur.left)
                    if cur.right is not None:
                        q.append(cur.right)

                    

                depth += 1

        
        bfs(root)
        return result
                

            