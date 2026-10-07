# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:#left less than current node not just locally but overall
    def isValidBST(self, root: Optional[TreeNode],min = float("-inf"),max = float("inf")) -> bool:
        if not root:
            return True #went through whole tree no violation

        if root.val <= min or root.val>= max:
            return False#whats at root is less than whats on left  and greater than whats on right

        return (self.isValidBST(root.left,min,root.val) and 
        self.isValidBST(root.right,root.val,max))

        


        
        