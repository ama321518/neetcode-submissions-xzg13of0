class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1#traking last two numbers this 1 and 2 ,remember the last two numbers before trak that number
        two = 1

        # you two are pur base variables ,one - 1 way to reah step 1

        #we need to save one bekause we are about to overwrute it
        for i in range(n-1):#starts here kuz answer for steo one already in
            temp = one
            one = one + two
            two = temp
        return one


