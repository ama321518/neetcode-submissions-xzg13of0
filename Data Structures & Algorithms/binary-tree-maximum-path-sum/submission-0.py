# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")
        def dfs(node):
            nonlocal best
            if not node:
                return 0

            left = max(dfs(node.left), 0)#if dfs at left gives positive takes that else if neg there we pick 0
            right = max(dfs(node.right), 0)
            best = max(best, (right+left) + node.val)
            return node.val + max(left, right)#when going through children to get the bigger

        dfs(root)
        return best
            



        