class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashmap = {}

       for i,nums in enumerate(nums):
        complement = target - nums
        if complement in hashmap:
            return [hashmap[complement],i]
        else:
            hashmap[nums] = i