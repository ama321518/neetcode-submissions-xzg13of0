class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input of intgers iam to return the length ofthe longest sequence , #our strtong point -use of nums-1 to check for running 

        seen = set(nums)
        max_length = 0

        for num in seen:#we loop through set so we dont rekhek duplikate vaues
            if num - 1 not in seen:#this checks for our starting point 
                count = 1
                next = num + 1#the next number im looking at in the chain
                while next in seen:
                    count+= 1
                    next += 1
                max_length = max(max_length,count)
        return max_length