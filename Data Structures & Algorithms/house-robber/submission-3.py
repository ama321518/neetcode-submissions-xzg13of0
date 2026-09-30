class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0 #two houses away

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 #rob1 gets old rob2 
            rob2 = temp
        return rob2#holds best answer

        #whole idea is max of what on plus next or two houses ago
        