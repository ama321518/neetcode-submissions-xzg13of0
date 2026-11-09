class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]],Output: true
        #base case
        if len(edges) != n-1:
            return False


        #node and its neighbors
        neighbors = {}
        for node in range(n):
            neighbors[node] = []
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
            


        #set and dfs walk
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in neighbors[node]:
                dfs(nei)
        dfs(0)
        return len(visited) == n


        #return


        