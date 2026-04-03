# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True] #a way to remeber if any node breaks the rule we are assuming and we need to keep running dfs till we hit a first problem then we stop caring
        def height(node):#helper to return the height
            if not node:
                return 0
            left_h = height(node.left)
            if balanced[0] is False:
                return 0
            right_h = height(node.right)
            if balanced[0] is False:
                return False
            if abs(left_h - right_h) > 1:
                balanced[0]= False
            return 1 + max(left_h,right_h)
        height(root)
        return balanced [0]