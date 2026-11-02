class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False#idea of if you have 5 friends you need 4 calls to link all 5,connections given and how many a tree needs 

        neighbors = {i: [] for i in range(n)}
        #neighbors = {}
            #for i in range(n):
                #neighbors[i] = []
            #n = 4 it makes {0: [], 1: [], 2: [], 3: []}

          #second part  for every edge [a, b] each neighbor to other to append    {0: [1, 2], 1: [0], 2: [0, 3], 3: [2]}
          
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
#Start at a node.
#If it’s already in visited, stop.
#Otherwise, add it to visited.
#Then do steps 2 and 3 again for every node in its neighbors list.
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in neighbors[node]:
                dfs(nei)

        dfs(0)#starts at the first node in our dictionary

        return len(visited) == n






        






        