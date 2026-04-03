class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #rebuilding over weekned with shrt example-[1 3 2 5](set ptrs ,best area so far,loop,get width ,get mini um height ,get area ,update best arae then the moving ptr ypu dp so when left smaller,move left or else right in then return max area)
        left = 0
        right = len(heights)-1

        best = 0

        while left < right:
            width = right - left #heiht[l-r] this is for height 
            #pick smaller of heihts since shorter is what we want if picked longer would pour out
            height = min(heights[left], heights[right])
            area = width * height 
            best = max(best, area)

            if heights[left] < heights[right]:
              left +=1
            else:
              right -=1
        return best
