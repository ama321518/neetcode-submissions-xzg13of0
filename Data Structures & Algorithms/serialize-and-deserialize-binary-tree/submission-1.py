# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        parts = []#the pieces of the string
        def dfs(node):
            if not node:
                parts.append("null")#we are writing down what we see one by one
            else:
                parts.append(str(node.val))

                dfs(node.left)
                dfs(node.right)
        dfs(root)

        return ",".join(parts)
      
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        position = 0
        parts_deserialise = data.split(",")

        def dfs():
            nonlocal position
            value = parts_deserialise[position]

            position += 1

            if value == "null":
                return None

            node = TreeNode(int(value))

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

       

        

