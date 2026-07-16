# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:#do an inorder traversal
        self.count = 0#track of nodes visited when it equals k yay answer
        self.result = None #stores k

        def helper(node):
            if not node:
                return None

            helper(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val

            helper(node.right)

        helper(root)
        return self.result


        