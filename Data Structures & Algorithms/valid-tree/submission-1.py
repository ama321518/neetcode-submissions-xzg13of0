class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #4 parts- the whole idea of if one comes to meet the other (a loop we return false) base check then hashmap setup the set check if already in if not add then do on the neighbor then in the end return length check to whats in hashmap i think that returns true or false 
        #Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]] , Output: true
        if len(edges) != n-1:
            return False

        neighbors = {}
        for node in range(n):
            neighbors[node] = []

        for a,b in edges:
            neighbors[b].append(a)
            neighbors[a].append(b)


        visited = set()

        def dfs(node):
            if node in visited:
                return node

            visited.add(node)

            for nei in neighbors[node]:
                dfs(nei)

        dfs(0)
        return len(visited) == n

            

        

        
        







        