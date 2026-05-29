class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best_min = float('inf')#if was zero would never update
        current = 0
        left = 0

        for right in range(len(nums)):
            current += nums[right]

            while current >= target:
                best_min = min(best_min, right - left + 1)
                current -=nums[left] 
                left += 1
        return 0 if best_min == float('inf') else best_min
            

        