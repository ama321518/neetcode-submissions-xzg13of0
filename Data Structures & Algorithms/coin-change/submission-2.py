class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we build up from zero
        #key thing to remember 1 + min of dp of amount minus koin gives the minimum ??

        dp = [float('inf')] * (amount + 1)#We fill with infinity because we don't know the answers yet. As we calculate each position we replace infinity with the real answer.amount + 1 because we need positions 0 through 6 — that's 7 spots.

        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        


        