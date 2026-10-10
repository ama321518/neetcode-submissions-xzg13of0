class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        def helper(houses):
            one = 0#one house bak
            two = 0#two houses bak

            for house in houses:#always remember to use helpers own parameters
                best = max(one, two + house)

                #order is the problem-remember its sortof like moving forward to next house to khek that whole kondition again
                #what was one house bak is now two houses bak
                two = one#one is now two houses bak
                one = best #one house bak is now the best 

            return one
        return max(helper(nums[1:]), helper(nums[:-1]))#everytning exkept first house or everything exkept last house 

        
        