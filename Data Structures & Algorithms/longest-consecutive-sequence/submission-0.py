class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #U - input is array of numbers and output is length of the max karakers that run next to eah other
         #M - what pattern here ???
         #sorting puts us in log n time so what other pattern ,from question the element on must be greater than prev element 
         #P - we will have a max_length stsrting at 0 we loop through then we khek if element we are on is greater than the previous if yes then add into kounter if not skip over it but my question must they be like numbers next to eah other or the previous one just has to 
        seen = set()
        
        for num in nums:
            seen.add(num)

        max_len = 0
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                max_len = max(length, max_len)

        return max_len
        