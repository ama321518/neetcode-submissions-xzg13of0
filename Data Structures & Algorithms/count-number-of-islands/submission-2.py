class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #base kase,getting set up of rows kolumns then kount then the two loops then seeing if island then inkreasing kount then kalling dfs then return 
        #then the dfs part a helper fxn then we do base kases where it goes down(rown) and left(kolumn) and right(kolumn) and above(row)
         #then kall dfs on four sides
        if not grid:
            return 0
    
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
    
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
    
        return islands

      