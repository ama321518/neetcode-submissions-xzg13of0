# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#1 + mmax(l,r)- the nide plus the left and right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0#the height
            #basically returning from lower the sum of the node heigtht back up
        left = self.maxDepth(root.left)#self because its in a class
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

        