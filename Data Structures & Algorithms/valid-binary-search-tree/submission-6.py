# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],min = float("-inf"),max = float("inf")) -> bool:#need to be in here ,you reset eveytime if outisde would be wiped out))
        if not root:
            return True

        if min >= root.val or root.val >= max:
            return False
        #else:
            #return True - dont pass in this bekause it lets you look at the node instead of also the kids
        return self.isValidBST(root.right,min=root.val,max= max) and self.isValidBST(root.left,max = root.val,min=min)



        