class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #tool- set to see what gone through and what havent gone through
        #insight- same walkthrough if already visited skip else add to set and increase count
        #shape
        #a counter then a set to 0 then look in set if not in add in if in skip then increase count then return count 

        #the neighbors lookup
        hashmap = {}
        for node in range(n):
            hashmap[node] = []

        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)

        #the visited set and the counter
        counter = 0

        visited = set()
        def dfs(node):
            if node in visited:
                return     
            visited.add(node)
            for nei in hashmap[node]:
                dfs(nei)
        #here we are looking at every node one by one, this is for making sure we check every node rememeber the example that went from 0 to 2 then 3 and 4 this part makes sure we check and add in
        #THE LOOP FINDS NEW GROUPS AND DFS FILLS THEM UP
        for node in range(n):
            if node not in visited:
                dfs(node)

                counter += 1
            

        return counter






        