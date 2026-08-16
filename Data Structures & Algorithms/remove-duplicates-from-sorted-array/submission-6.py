class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1 1 2

        write = 1

        for scan in range(1, len(nums)):
            if nums[scan] != nums[scan -1]:
                #remember it doesnt se duplicate so move forward first ,inside dupivate automatically skipped
                nums[write]= nums[scan]
                write += 1
                
         
        return write
                








































