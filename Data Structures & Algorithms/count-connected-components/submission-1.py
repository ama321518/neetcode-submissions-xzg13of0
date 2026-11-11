class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #hashmap
        hashmap = {}
        for node in range(n):
            hashmap[node] = []

        for a,b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)


        #count and set
        counter = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in hashmap[node]:
                dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                counter += 1

        return counter

        
            

        

        #part making sure you go through second part 

        #return
        