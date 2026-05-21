class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)- 1

        best = 0
            
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l

            area = height * width

            best = max(area,best)
            if heights[l]< heights[r]:
                l += 1
            else:
                r -= 1

        
        
    
        return best
        
        
            #rebuilding over weekned with shrt example-[1 3 2 5](set ptrs ,best area so far,loop,get width ,get mini um height ,get area ,update best arae then the moving ptr ypu dp so when left smaller,move left or else right in then return max area)
        

        
            


        