class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left and right defined ,middle defined then check if equal to target then check if target now within fit and decide which direction to move in
        #do same for right then return -1 in the whole end

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1      
                else:
                     right = mid - 1 
        return -1
                    


        