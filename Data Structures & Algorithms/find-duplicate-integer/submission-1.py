class Solution:
    def findDuplicate(self, nums: List[int]) -> int:#
        slow = 0
        fast = 0

        while True: #while we always have valid indexes
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0 #if you reset and start and make both move at the same time theyll meet at the duplicate

        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow


