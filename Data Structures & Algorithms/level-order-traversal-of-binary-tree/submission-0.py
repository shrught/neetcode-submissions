# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        depth = 1

        while q:
            sz = len(q)
            cur_level = []
            for i in range(sz):
                cur = q.popleft()
                ##
                cur_level.append(cur.val)

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            res.append(cur_level)
            depth += 1
        

        return res

