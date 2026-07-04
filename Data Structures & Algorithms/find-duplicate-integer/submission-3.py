class Solution:
    def findDuplicate(self, nums: List[int]) -> int:#
        slow = nums[0]
        fast = nums[0]

        while True: #while we always have valid indexes
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0] #if you reset and start and make both move at the same time theyll meet at the duplicate

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

            
        return slow


