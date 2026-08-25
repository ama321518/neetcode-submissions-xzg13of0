class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)- 1

       

        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            #after we have the pieces together its time to figure out which part left or right is fully sorted

            if nums[left] <= nums[mid]:#our sorted is in left
                if nums[left]<= target<= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 #for finding target in this part
            elif nums[right]>= nums[mid]:
                if nums[right]>= target>= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        if nums[left] == target:
            return left
        return -1

            

        