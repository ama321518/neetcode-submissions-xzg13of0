class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        sum_looking_at = nums[0]

        for i in range(1, len(nums)):
            sum_looking_at = max(sum_looking_at + nums[i], nums[i])#restart from number looking on or add in
            best = max(best,sum_looking_at)
        return best