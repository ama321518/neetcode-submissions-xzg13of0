class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True  # Return True as soon as a duplicate is found
            hash_set.add(num)
        return False 