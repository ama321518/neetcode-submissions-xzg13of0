class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 0 0 3
        write = 0
        for scan in range(len(nums)):
            if nums[scan]!= 0:
                nums[write]= nums[scan]
                write += 1
                
        #here we get to where filling in zeroes need another loop

        for i in range(write,len(nums)):
            nums[i] = 0



        #here is what i am thinking for every number we are on if that number is equal to zero we swap positions with the one to the right of it then we swap again with next right then next until we reach end we keep doing this till all zeroes are in the end this is the idea i ahve but now its the code writing 

       
#ptr is our secom\nd ptr which marks where valid stuff go-keeps track of the non zeroes going to the front
#we use range len cuz we are modifying so need index
#we check not equal cuz thts what goes infront 

            