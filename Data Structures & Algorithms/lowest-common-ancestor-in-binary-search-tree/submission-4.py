# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return

            #always ask self the condition that makes p and q move left then ask self the condition that makes p and q move right-remember what it means for left and right and then for the two of the eah think of the 

        if p.val < root.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)

        elif p.val > root.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root



        
        