# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #level order the first idea is queues going level by level then if a root has children add into queue then pop for the next level to get in import deque then create empty list then base case if theres nothing in list return empty list then loop through then if we see a node add into queue then pop then append into new list we create to have that list of lists then do for left and right child then finally append that list to result and return result time -loop o(n) popping from queue 0(1),space 0(n)-creating new list

        q = deque([root])
        result = []

        if not root:
            return []


        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result




        