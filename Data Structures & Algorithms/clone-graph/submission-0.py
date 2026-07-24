"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

       
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]#to prevent double kounting

            hashmap[node] = Node(node.val)#store kopy of node so its old to new

            #neighbor part
            for neighbor in node.neighbors:
                 hashmap[node].neighbors.append(dfs(neighbor))
            return hashmap[node]

        return dfs(node)



        

        