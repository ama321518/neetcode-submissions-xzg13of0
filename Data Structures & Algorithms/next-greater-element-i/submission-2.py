class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                prev_num = stack.pop()

                hashmap[prev_num] = num

            stack.append(num)

        result = []
        for num in nums1:
            if num in hashmap:
                result.append(hashmap[num])
            else:
                result.append(-1)
        return result           
            
        