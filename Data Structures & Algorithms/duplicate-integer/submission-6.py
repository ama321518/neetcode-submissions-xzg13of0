class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


       
        
        

        #given input array rrtuen boolen false ,no small length contraint,edge case if one lement return false since doesnt appear twice
       #our ds here would be a set it allows us to see when an elemnt is two,our approah we kreate set ,we loop through num if that number in nums in set we return true if not we add in number then at end return false if went through all and didnt see anything
       