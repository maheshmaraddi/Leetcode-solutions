class Solution:
    def maxProfit(self, Arr: List[int]) -> int:
        n=len(Arr)
        dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
    
    # Base condition: Initialize the last row of DP table to 0 since there are no more days to trade
        dp[n][0] = dp[n][1] = 0
        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                
                if buy == 0:
                    # We can buy the stock
                    profit = max(0 + dp[ind + 1][0], -Arr[ind] + dp[ind + 1][1])
                elif buy == 1:
                    # We can sell the stock
                    profit = max(0 + dp[ind + 1][1], Arr[ind] + dp[ind + 1][0])
                
                dp[ind][buy] = profit  # Store the result in the DP table
        
        return dp[0][0]
                
        