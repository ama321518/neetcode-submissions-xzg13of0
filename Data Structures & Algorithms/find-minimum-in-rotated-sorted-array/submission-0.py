class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]#binary searh kuz want fast lookup of that smallest number,so you know your binary set up the konfusing part is when the nu,ber at mid is less than whats at right right gets mid value then at end always remeber tht left is gonna get to rights value so we do return nums[left] / we kould do nums[right]it automatikally equals the answer is there i hope this makes sense


                