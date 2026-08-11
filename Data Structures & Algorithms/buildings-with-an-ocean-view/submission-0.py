class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_so_far = 0
        result = []
        
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_so_far:
                result.append(i)
                max_so_far = heights[i]
        
        result.reverse()
        return result
        