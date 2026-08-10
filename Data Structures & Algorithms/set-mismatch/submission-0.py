class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        dup = None
        
        for num in nums:
            if num in seen:
                dup = num
            else:
                seen.add(num)
        
        missing = (set(range(1, n+1)) - set(nums)).pop()
        return [dup, missing]



        