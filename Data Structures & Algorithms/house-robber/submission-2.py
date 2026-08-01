class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back = 0   # best answer two houses ago
        one_back = 0   # best answer one house ago

        for n in nums:
            temp = max(n + two_back, one_back)
            two_back = one_back
            one_back = temp

        return one_back
                