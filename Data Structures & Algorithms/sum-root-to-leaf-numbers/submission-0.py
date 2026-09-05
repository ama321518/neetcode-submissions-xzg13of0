# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,current_number):
            if not root:
                return 0

            current_number = current_number * 10 + root.val

            if not root.left and not root.right:
                return current_number

            return dfs(root.left,current_number) + dfs(root.right,current_number)

        return dfs(root,0)
        