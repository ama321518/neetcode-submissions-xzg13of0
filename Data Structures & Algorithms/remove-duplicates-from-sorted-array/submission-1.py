class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1 1 2

        write = 0

        for scan in range(1,len(nums)):
            if nums[scan] != nums[write]:
                write += 1
                nums[write] = nums[scan]
        k = write + 1
        return k
                