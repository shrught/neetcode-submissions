# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return
        #conditions: when both p and q value are larger than current node, traverse the right subtree
        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        #if both p and q are smaller than current node, traverse the left subtree
        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
