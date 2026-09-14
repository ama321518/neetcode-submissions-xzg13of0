# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #ideas from the question - how deep can i go left and how deep can i go right
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            height = max(right,left)+ 1
            self.diameter = max(right+left,self.diameter)
            return height
            

        dfs(root)
        return self.diameter


       


        