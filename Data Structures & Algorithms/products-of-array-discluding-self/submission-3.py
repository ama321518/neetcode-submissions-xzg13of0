class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input is array of nums and output is product of all the other numbers except itself,constraint nothing unusual edge case if only one element we return zero i guess theres nothing before and there's nothing after.
        #approach from what i remember th two psrts where suffix and prefix we start with creating a list with nums all multiplied by 1 to fill it,lets strt with prefix we set it 0 then we loop through nums then we do prefix[nums] times like next numbersss then for suffix to same idea then we multiply prefix with suffix 

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]* nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i + 1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result




        