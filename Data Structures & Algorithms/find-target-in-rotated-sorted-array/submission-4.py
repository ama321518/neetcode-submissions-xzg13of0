class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #mistakes made: mid was outside the loop it needs to be in,always remember that if its outside as left and the right changes if mid updated once it would not get updates 
    #sorted already 

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:#checking with sorted half
                if  nums[left] <= target < nums[mid]:#looks at target fit
                    right = mid -1 #this skips all everything over right side
                else:
                    left = mid + 1 #if not in left skip over all in left then move to right

            else:
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1 #skip over all left since found target in right
                else:
                    right = mid - 1

        return -1


                    
                    
            


