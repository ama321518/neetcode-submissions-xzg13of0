class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given two inputs an integer and a target i am to find two numbers in here that add up to that target given.a constraint is that our two indices wont be the same,an edge case is that we wont have an empty array
        #question is what data structure allows us to have lookup of numbers a stack no,ques,two pointers here no ,a set no so im thinking a hashmap here we would look into to see hey do our two numbers exist in here that add up to target??
        #start with creating hashmap then we loop through nums then ask if the other number in hashmap if yes return indices of number and other number if not add number to hashmap
        hashmap = {}

        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num],i]
            else:
                hashmap[num] = i

    #time complexity - would be o(n)
    #space complexity - would be o(n)
